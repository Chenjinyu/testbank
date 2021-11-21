import sys
import os
import logging
import time, datetime
import fnmatch
from os import makedirs, walk, stat, walk
from os.path import join, exists


__version__ = '1.0.1'

'''
version 1.0.0
        basic functions
version 1.0.1
        add: delete un-necessnary log files after some days(the days need to be defined).
'''


def get_current_script_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def getCurrentDate():
    return datetime.datetime.now().strftime("%Y_%m_%d")


def remove(path, retries=3):
    """
    Remove one file
    """
    if not exists(path):
        raise IOError('File %s not exist' % path)

    for i in range(1, retries + 1):
        try:
            os.remove(path)
            break
        except OSError as e:
            logging.debug('Fail %d times: %s' % (i, e))
            if i > 0:
                time.sleep(1)
            else:
                raise


class _LogConfig(object):
    """
    logging library.
    Author: Eleven_Chen@symantec.com
    Date: 2013-03-16
    """

    LOG_LEVEL_LIST = {'debug': logging.DEBUG,
                      'info': logging.INFO,
                      'warn': logging.WARNING,
                      'warning': logging.WARNING,
                      'error': logging.ERROR,
                      'critical': logging.CRITICAL}

    def __init__(self, level=None, days_del_log=30):

        if level is None:
            level = 'notset'
        self.logger = logging.getLogger()
        self.log_level = _LogConfig.LOG_LEVEL_LIST.get(level.lower(), logging.NOTSET)
        self.logger.setLevel(self.log_level)
        self.current_running_script_name = get_current_script_name()
        if days_del_log > 0:  # days_del_log = -1 is doesn't delete
            self._delete_old_log_files_by_days(days_del_log)

    def _output_log_to_file(self, file_name=None):
        """
        output log information to log file
        @var file_name: string. if file_name is None, it will name the log file as: [script_name]_[current_date].log
        """

        file_path = '../log/'
        if file_name is None:
            file_name = self.current_running_script_name

        full_file_path = join(file_path, file_name)
        file_name = file_name + '_' + getCurrentDate() + '.log'

        if not exists(full_file_path):
            makedirs(full_file_path)
        try:
            file_handler = logging.FileHandler(join(full_file_path, file_name))
            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(self._logging_simple_formatter())
            self.logger.addHandler(file_handler)
        except Exception as e:
            print("**[ERROR]** error happen: %s" % e)
            raise

    def _delete_old_log_files_by_days(self, days_del_log):
        """
        delete old log file, the default is ON
        """
        current_time = datetime.datetime.now()
        for root, dirs, log_files in walk(join('../log/', self.current_running_script_name)):
            for file in log_files:
                if fnmatch.fnmatch(file, self.current_running_script_name + '_*.log'):
                    file_modify_time = time.localtime(stat(join(root, file)).st_mtime)
                    formatted_modify_time = datetime.datetime(file_modify_time[0],
                                                              file_modify_time[1],
                                                              file_modify_time[2],
                                                              file_modify_time[3])

                    dis_days = (current_time - formatted_modify_time).days
                    if dis_days >= days_del_log:
                        remove(join(root, file))

    def _output_log_to_console(self):
        """
        output log information to console
        """
        try:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            console_handler.setFormatter(self._logging_simple_formatter())
            self.logger.addHandler(console_handler)
        except Exception as e:
            print("**[ERROR]** error happen: %s" % e)
            raise

    def _logging_formatter(self):
        return logging.Formatter("%(asctime)s:[%(levelname)s][%(module)s.%(funcName)s]: %(message)s",
                                 "%Y-%m-%d %H:%M:%S")

    def _logging_simple_formatter(self):
        return logging.Formatter("%(asctime)s:[%(levelname)s]: %(message)s", "%Y-%m-%d %H:%M:%S")

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self.warning(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)


class FileLogConfig(_LogConfig):

    def __init__(self, file_name=None, level=None, days_del_log=30):
        _LogConfig.__init__(self, level, days_del_log)
        self._output_log_to_file(file_name)


class ConsoleLogConfig(_LogConfig):

    def __init__(self, level=None, days_del_log=30):
        _LogConfig.__init__(self, level, days_del_log)
        self._output_log_to_console()


class FileAndConsoleLogConfig(_LogConfig):

    def __init__(self, file_name=None, level=None, days_del_log=30):
        _LogConfig.__init__(self, level, days_del_log)
        self._output_log_to_file(file_name)
        self._output_log_to_console()


if __name__ == "__main__":
    # test
    test = FileAndConsoleLogConfig()
    test.info('ff')