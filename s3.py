from __future__ import absolute_import
import time
import os
import urllib2
import StringIO

import boto

from sister_core.sister_logger import log


def connect():
    return boto.connect_s3('0KMZHPQ56ZMG07Q3HG02', 'dxPbBh++Fja9vZvkVyMksb1mgnCDetcfV8mNy+9+', is_secure=False)


def upload_file(bucket, s3_key, local_path, s3_connection=None, policy='public-read', max_retries=3):
    if not os.path.exists(local_path):
        message = "File does not exist locally - {} - {} -- {}}".format(bucket, local_path, s3_key)
        log.critical(message)
        return {"status": "FAILURE", "Message": message}
    # print s3_key
    if s3_key.startswith('/'):
        s3_key = s3_key[1:]

    retry = 1
    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection is not None else connect()
            s3_bucket = s3.get_bucket(bucket)
            key = s3_bucket.get_key(s3_key)
            if not key:
                key = s3_bucket.new_key(s3_key)

            if key.set_contents_from_filename(local_path, policy=policy):
                url = key.generate_url(0, query_auth=False, force_http=True)
                message = "Successfully uploaded the file to s3 - {} - {} - {}".format(bucket, local_path, s3_key)
                log.info(message)
                return {"status": 'SUCCESS', 'URL': url, "Message": message}
            else:
                message = "Failed to upload file to s3 - {} - {}".format(bucket, local_path, s3_key)
                log.warning('')
                return {"status": 'FAILURE', "Message": message}
        except RuntimeError as e:
            if retry < max_retries:
                log.warning('Error ({}/{}) trying to upload file - bucket: {} key: {} path {} error: {}'.format(
                    retry,
                    max_retries,
                    bucket,
                    s3_key,
                    local_path,
                    e.message,
                ))
                retry += 1
                time.sleep(1)
            else:
                message = "Failed to upload to S3 - bucket: {} key: {} path {} error: {}".format(
                    bucket,
                    s3_key,
                    local_path,
                    e.message,
                )
                log.critical(message)
                return {"status": "FAILURE", 'Message': message}


def upload_folder(bucket, s3_key, local_path, s3_connection=None, policy='public-read', max_retries=3):
    if s3_key.startswith('/'):
        s3_key = s3_key[1:]

    if not os.path.exists(local_path):
        message = "Folder doesn't exist - bucket: {} key: {} path: {}".format(bucket, s3_key, local_path)
        log.critical(message)
        return {'status': 'FAILURE', 'Message': message}
    walked_directory = os.walk(local_path)
    for (file_path, dir_name, file_names) in walked_directory:
        for file_name in file_names:
            local_file_path = str(os.path.join(file_path, file_name))
            file_key = local_file_path.replace(local_path, s3_key)
            upload_file(
                bucket,
                file_key,
                local_file_path,
                s3_connection=s3_connection,
                policy=policy,
                max_retries=max_retries,
            )
    message = 'Finished uploading folder to s3 - bucket: {} key: {} path: {}'.format(bucket, s3_key, local_path)
    log.info(message)
    return {'status': 'SUCCESS', 'Message': message}


def download_file(bucket, s3_key, file_path, s3_connection=None):
    retry = 1
    max_retries = 3
    if s3_key.startswith('/'):
        s3_key = s3_key[1:]

    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection is not None else connect()
            s3_bucket = s3.get_bucket(bucket)
            key = s3_bucket.get_key(s3_key)
            if not key:
                message = 'Key does not exist on s3 - bucket: {} key: {} path: {}'.format(bucket, s3_key, file_path)
                log.critical(message)
                return {'status': 'FAILURE', 'Message': message}

            dir_name = os.path.dirname(file_path)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            key.get_contents_to_filename(file_path)
            message = "Successfully downloaded file from s3 - bucket {} key: {} path: {}".format(
                bucket,
                s3_key,
                file_path,
            )
            log.info(message)
            return {"status": "SUCCESS", "Message": message}
        except RuntimeError as e:
            if retry < max_retries:
                log.warning("Error ({}/{}) try to download file - bucket {} key: {} path: {} error: {}".format(
                    retry,
                    max_retries,
                    bucket,
                    s3_key,
                    file_path,
                    e.message,
                ))
                retry += 1
                time.sleep(1)
            else:
                message = "Failed to download from S3 - bucket {} key: {} path: {} error: {}".format(
                    bucket,
                    file_path,
                    s3_key,
                    e.message,
                )
                log.critical(message)
                return {"status": "FAILURE", "Message": message}


def delete_file(bucket, s3_key, s3_connection=None, max_retries=3):
    """Method to remove specific file from s3.
    Args:
        s3_connection (class, optional): s3 connection object, defaults to None.
        max_retries (int): number of times to try and execute method.
    """
    retry = 1
    log.info('Attempting to remove file from s3 - {} - {}'.format(bucket, s3_key))
    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection is not None else connect()
            s3_bucket = s3.get_bucket(bucket)
            key = s3_bucket.get_key(s3_key)
            if not key:
                message = "s3 key does not exist - {} - {}".format(bucket, s3_key)
                log.warning(message)
                return {"status": 'FAILURE', "Message": message}
            resp = key.delete()
            log.debug("Removing file from s3 - {} - {} -- {}".format(bucket, key, resp))

            return {"status": 'SUCCESS', "Message": "removed s3 key - {} - {}".format(bucket, s3_key)}
        except RuntimeError as e:
            retry += 1
            time.sleep(1)
            log.error("Error connecting to s3 - {} - {} -- {}".format(bucket, s3_key, e))
            if retry <= max_retries:
                continue
            else:
                message = "Possible connection issues. Failed deleting the file from s3 - {} - {}".format(
                    bucket,
                    s3_key,
                )
                return {"status": 'FAILURE', "Message": message}


def delete_folder(bucket, s3_key, s3_connection=None, max_retries=3):

    retry = 1
    log.info('Attempting to remove file from s3 - {} - {}'.format(bucket, s3_key))
    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection is not None else connect()
            s3_bucket = s3.get_bucket(bucket)

            bucket_list = s3_bucket.list(s3_key)
            log.debug("Removing folder from s3 - {} - {}".format(bucket, s3_key))
            result = s3_bucket.delete_keys([key.name for key in bucket_list])
            log.debug("Successfully removed folder from s3 - {} - {}".format(bucket, s3_key))
            return {"status": 200, "Message": "Successfully removed folder from s3 - {} - {}".format(bucket, s3_key)}
            # if len(delete_key_list) > 0:
            #     s3_bucket.delete_keys(delete_key_list)

        except RuntimeError as e:
            retry += 1
            time.sleep(1)
            continue
    return {"status": 400, "Message": "Failed removing folder from s3 - {} - {}".format(bucket, s3_key)}


def walk_folder(bucket, dir_key, s3_connection=None, max_retries=3):
    """Method that walks and s3 folder and returns all children of that folder.
    Args:
        s3_connection (class, optional): s3 connection object, defaults to None.
        max_retries (int): number of times to try and execute method.
    Returns:
        dict: returns response dict. If process successful has 'walk_list' field
            that contains s3 keys of the provided directory children.
    """
    # make sure there are no slashes at the start of the path
    if dir_key.startswith('/'):
        dir_key = dir_key[1:]
    retry = 1

    log.info("Attempting to retrieve bucket list - {} - {}".format(bucket, dir_key))
    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection is not None else connect()
            s3_bucket = s3.get_bucket(bucket)
            walk_list = []
            bucket_list = s3_bucket.list(dir_key)
            for key in bucket_list:
                walk_list.append(key)

            message = "Finished getting directory list - bucket :{} key: {} walk_list: {}".format(
                bucket,
                dir_key,
                walk_list,
            )
            log.info(message)
            return {"status": "SUCCESS", "walk_list": walk_list, "Message": message}
        except RuntimeError as e:
            if retry < max_retries:
                log.warning("Error ({}/{}) in getting folder list - bucket :{} key: {} error: {}".format(
                    retry,
                    max_retries,
                    bucket,
                    dir_key,
                    e.message,
                ))
                retry += 1
                time.sleep(1)
                continue
            else:
                message = "Failed getting folder list - bucket :{} key: {} error: {}".format(bucket, dir_key, e.message)
                log.warnig(message)
                return {"status": "FAILURE", "Message": message}


def exists(bucket, s3_key, s3_connection=None):
    max_retries = 3
    retry = 1

    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection else connect()
            search_bucket = s3.get_bucket(bucket)
            key = search_bucket.get_key(s3_key)

            if key:
                message = 'Key exists - bucket {} key: {}'.format(bucket, s3_key)
                log.info(message)
                return {'status': 'SUCCESS', 'KEY': key, 'Message': s3_key}
            else:
                message = "Key doesn't exists - bucket {} key: {}".format(bucket, s3_key)
                log.info(message)
                return {'status': 'SUCCESS', 'KEY': key, 'Message': s3_key}
        except Exception as e:
            if retry < max_retries:
                log.critical("Failed checking existence of key - bucket: {} key: {} error: {}".format(
                    retry,
                    max_retries,
                    bucket,
                    s3_key,
                    e.message,
                ))
                retry += 1
                time.sleep(1)
                continue
            else:
                message = "Failed to access S3 key or bucket - bucket: {} key: {} error: {}".format(
                    bucket,
                    s3_key,
                    e.message,
                )
                return {"status": "FAILURE", "Message": message}

    # raise RuntimeError('Failed to check file exists for: {}:{}'.format(bucket, s3_key))


def copy_file(start_bucket, start_key, end_key, end_bucket=None, s3_connection=None, max_retries=3):
    """Method copies files around s3.
    Args:
        s3_connection (class, optional): s3 connection object, defaults to None.
        max_retries (int): number of times to try and execute copy.
    Returns:
        dict: returns response dict with SUCCESS or FAILURE depending on outcome.
    """
    log.info('IN COPY FILE')
    retry = 1
    log.debug("copying file {} - {} - {}".format(start_bucket, start_key, end_key, end_bucket))
    # if not isinstance(start_key, boto.s3.key.Key):
    if type(start_key) == str or type(start_key) == unicode:
        if start_key[:1] == '/':
            start_key = start_key[1:]

    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection else connect()
            if isinstance(start_key, boto.s3.key.Key):
                log.info('Found a boto instance - {} - {}'.format(start_bucket, start_key))
                if end_bucket:
                    destination_bucket = s3.get_bucket(end_bucket)
                    start_key.copy(destination_bucket, end_key, preserve_acl=True)
                else:
                    destination_bucket = s3.get_bucket(start_bucket)
                    start_key.copy(destination_bucket, end_key, preserve_acl=True)

                url = destination_bucket.new_key(end_key).generate_url(0, query_auth=False, force_http=True)

                return {"status": 'SUCCESS', 'URL': url, "Message": "Copied file to new bucket - {} -- {}".format(end_bucket, end_key)}
            else:
                log.info('Not a boto instance - bucket: {} key: {}'.format(start_bucket, start_key))
                start_bucket = s3.get_bucket(start_bucket)
                destination_bucket = s3.get_bucket(end_bucket)
                key = start_bucket.get_key(start_key)
                log.debug("s3 Key that was found bucket: {} start_key: {} key: {}".format(start_bucket, start_key, key))
                if key:
                    if destination_bucket:
                        key.copy(destination_bucket, end_key, preserve_acl=True)
                    else:
                        start_key.copy(start_key.bucket, start_key.key, preserve_acl=True)

                    url = destination_bucket.new_key(end_key).generate_url(0, query_auth=False, force_http=True)
                    message = "Copied file to new bucket - bucket: {} key: {}".format(end_bucket, end_key)
                    log.info(message)
                    return {"status": 'SUCCESS', 'URL': url, "Message": message}
                else:
                    message = "copying file to new bucked failed. Key doesn't exist - {} -- {}".format(end_bucket, end_key)
                    log.warning(message)
                    return {"status": 'FAILURE', "Message": message}

        except RuntimeError as e:
            if retry < max_retries:
                log.warning("Error ({}/{}) trying to copy file - start_bucket: {}  start_key: {} error: {}".format(
                    retry,
                    max_retries,
                    start_bucket,
                    start_key,
                    e.message,
                ))
                retry += 1
                time.sleep(1)
                continue
            else:
                message = "Failed copying file - start_bucket: {} " \
                          "start_key: {} end_bucket: {} end_key: {} error {}".format(
                    start_bucket,
                    start_key,
                    end_bucket,
                    end_key,
                    e.message,
                )
                log.critical(message)
                return {"status": "FAILURE", "Message": message}


def copy_dir(start_bucket, start_dir_key, end_dir_key, new_name=None, old_name=None, end_bucket=None, s3_connection=None):
    if start_dir_key[:1] == '/':
            start_dir_key = start_dir_key[1:]

    walk_response = walk_folder(start_bucket, start_dir_key, s3_connection)
    if walk_response['status'] == 'FAILURE':
        return walk_response

    walk_file_list = walk_response['walk_list']
    for s3_key in walk_file_list:
        file_path = s3_key.key.split(start_dir_key)[1]
        if new_name:
            file_path = file_path.replace(old_name, new_name)
        end_key = end_dir_key+file_path
        copy_file(start_bucket, s3_key, end_key, end_bucket, s3_connection)


def rename_file(bucket, old_key, new_key, s3_connection=None):
    max_retries = 3
    retry = 1
    log.debug("{} - {} - {}".format(bucket, new_key, old_key))
    if old_key[:1] == '/':
        old_key = old_key[1:]

    while retry <= max_retries:
        try:
            s3 = s3_connection if s3_connection else connect()
        except Exception as e:
            log.critical("Failed to connect or access S3 - {} -- {}".format(old_key, e))
            retry += 1
            time.sleep(1)
            continue

        try:
            search_bucket = s3.get_bucket(bucket)
            key = search_bucket.get_key(old_key)
            log.debug("s3 Key that was found - {} -- key {}".format(key, old_key))
        except Exception as e:
            log.critical("Failed to access S3 key or bucket - {} -  -- {}".format(bucket, old_key, e))
            return {"status": 400,
                    "Message": "Failed to access S3 key or bucket - {} -  -- {}".format(bucket, old_key, e)}

        try:

            key.copy(bucket, new_key, preserve_acl=True)
            key.delete()

            return {"status": 200, "Message": "Copied file to new bucket - {} -- {}".format(bucket, key)}
        except Exception as e:
            log.critical("Failed copying file to new bucket - {} - {} -- {}".format(bucket, key, e))
            return {"status": 400,
                    "Message": "Failed copying file to new bucket - {} - {} -- {}".format(bucket, key, e)}

    return {"status": 400,
            "Message": "Failed to connect tp s3 - {}".format(old_key)}