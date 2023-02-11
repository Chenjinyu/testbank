from config.LogConfig import FileAndConsoleLogConfig
import test
logging = FileAndConsoleLogConfig()

logging.info('starting logging')

test.test_fun()

logging.info('end logging')