from __future__ import absolute_import
import time
import os

import boto3


from botocore.exceptions import ClientError

__all__ = ['s3_file', 's3_folder']

class _S3(object):
    """
    Base S3 boto wrapper that handles core methods for assets.
    Args:
        bucket (str): S3 bucket to work from
        key (str): S3 key for asset
    Attributes:
        error (boolean): For error checking on object
        message (str): Message provided when errors occur or process finished
        policy (str): policy for when upload data. Default set to public-read
    Raises:
        S3ResponseError: When failing to communicate with S3 or errors occur in communication
    """

    def __init__(self, bucket, key):

        self._s3_client = self._get_s3_client()
        self._bucket = None
        self._key = None


    @property
    def bucket(self):
        """boto3 class: Instantiated boto3 object of the bucket"""
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        try:
            self._bucket = self.s3_client.Bucket(bucket)
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                print('Bucket: {} does not exist.')



    @property
    def s3_client(self):
        """boto class: Instantiated boto3 client object."""
        return self._s3_client

    @property
    def exists(self):
        """boolean: Simple existence check on files in S3"""
        return True if self.key else False

    @property
    def key(self):
        """boto class: Instantiated boto object of the key if value otherwise none"""
        return self._key

    @key.setter
    def key(self, key):
        if type(key) is str or type(key) is unicode:
            self._key = self.bucket.get_key(key)
        else:
            # Must be an s3 key object
            self._key = key
        # print self.key.key
        # log.info('S3 key: {}'.format(str(self.key)))

    @staticmethod
    def get_current_date():
        from datetime import datetime as dt
        current_date = dt.now().strftime("%m%d%Y")
        return current_date


    def _get_s3_client(self, max_retries=3):
        """Create a resource service client by name using the default session.
        Args:
            max_retries (int): Number of times to attempt to create a resource service client to s3
        Returns: S3 resource client or self object
        """
        retry = 1
        while retry <= max_retries:
            try:
                s3_client = boto3.resource('s3')
                return s3_client

            except Exception as e:
                if retry < max_retries:
                    print('Error ({}/{}) attempting to create s3 client - error: {}'.format(retry,
                                                                                 max_retries,
                                                                                 e.message,
                                                                                 ))
                    retry += 1
                    time.sleep(1)
                else:
                    message = "Failed connecting to S3 - error: {}".format(e.message)
                    print(message)
                    self.error = True
                    self.message = message
                    return self


class S3File(_S3):
    """
    Class Boto wrapper for handling AWS S3 files
    """
    @property
    def url(self):
        """str: Url string for asset"""
        if self.key:
            print self.key
            return self.key.generate_url(0, query_auth=False, force_http=True)
        else:
            return None

    @property
    def secure_url(self):
        """str: Url string for asset"""
        if self.key:
            # print self.key
            return self.key.generate_url(0, query_auth=False, force_http=False).replace('http:', 'https:')
        else:
            return None

    def download(self, file_path):
        """Method for download individual files from AWS S3 to a local file path
        Args:
            file_path (str): Path for where the file will download to
        Returns:
            True if asset exists locally, False otherwise
        """
        log.info('Downloading file: {}'.format(self.key))
        download_folder = os.path.dirname(file_path)
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # TODO 'NoneType' object has no attribute 'get_content_to_filename' bug
        self.key.get_contents_to_filename(file_path)

        if os.path.exists(file_path):
            return True
        else:
            return False

    def upload(self, file_path, file_key, policy=None):
        """Method for uploading assets to AWS S3
        Args:
            file_path (str): Local path of asset to be uploaded
            file_key (str): Desired key for the asset
            policy (str): Optional policy for overriding the default permissions
        """
        log.info('Uploading file to AWS: {}'.format(file_key))
        set_policy = policy if policy else self.policy
        if os.path.exists(file_path):
            if type(self.bucket.name) == unicode or type(self.bucket.name) == str:
                self.key = self.bucket.new_key(file_key)
            else:
                self.key = self.bucket.name.new_key(file_key)
            self.key.set_contents_from_filename(file_path, policy=set_policy)
            log.info('Local File Path: {}'.format(file_path))
        return self

    def delete(self):
        """Method for deleting asset from AWS S3
        returns:
            True if deletion from S3 successful, otherwise False
        """
        if self.key:
            self.key.delete()
            return True
        else:
            return False

    def copy_file(self, destination_bucket=None, destination_key=None):
        """Method for copying files around AWS S3
        returns:
            class object with attributes like url, error, message, key
        """
        # Make sure destinatino key and bucket weren't both set to none
        if not destination_bucket and not destination_key:
            self.error = True
            self.message = "Both destination_key and destination_bucket can't be set to None value"
            return self

        if destination_key == self.bucket and destination_key == self.key:
            self.error = True
            self.message = "Both destination_key and destination_bucket can't equal original key and bucket"
            return self

        if self.key:
            dest_bucket = destination_bucket or self.bucket.name
            dest_key = destination_key or self.key

            # Get the destination bucket
            coppied_file = self.key.copy(dest_bucket, dest_key, preserve_acl=True)

            # Only update the bucket if a new bucket was passed in
            if destination_bucket:
                self.bucket = destination_bucket

            self.key = coppied_file.key

            return self
        else:
            log.warning("Original Key does not exist on S3: {}".format(self.key))
            print "Original Key does not exist on S3: {}".format(self.key)
            # raise ValueError("Original Key does not exist on S3")

    @property
    def walk_folder(self):
        """Method that walks the folder the asset/file is located in.
        Returns:
            list: of s3 key objects.
        """
        assets_folder = os.path.dirname(self.key.key)
        raw_asset_lsit = self.bucket.list(assets_folder)
        asset_list = []
        for asset in raw_asset_lsit:
            asset_list.append(asset)

        return asset_list


class S3Folder(_S3):
    """
    Class Boto wrapper for handling AWS S3 'folders'
    Attributes:
       upload_list (list): list of boto key's for files to be uploaded from a local folder
    """
    def __init__(self, bucket, key):
        super(S3Folder, self).__init__(bucket, key)
        self.folder_list = None
        self.dirs_list = None

    @property
    def url_list(self):
        """Method for generating url list on the fly for uploaded assets
        Returns:
            list of urls if a url can be generated from the keys or none if empty list
        """
        if self.folder_list:
            url_list = []
            for key in self.folder_list:
                url_list.append(key.generate_url(0, query_auth=False, force_http=True)) if key else None
            return url_list if len(url_list) else None
        # elif self.url_list:
        #     return None
        else:
            print self.url_list
            return None

    def upload(self, folder_path, folder_key):
        """Method for uploading a local folder to AWS S3
        Args:
            folder_path (str): File path to the local folder to be uploaded
            folder_key (str): Base 'folder' key for the assets being uploaded
        Returns:
            self
        """
        log.info('Uploading folder: {}'.format(folder_key))
        walked_directory = os.walk(folder_path)
        upload_list = []
        for (root_file_path, dir_name, file_names) in walked_directory:
            for file_name in file_names:
                # if not 'DS_Store' in file_name:
                file_path = str(os.path.join(root_file_path, file_name))
                file_key = file_path.replace(folder_path, folder_key)
                s3_f = s3_file(self.bucket, file_key)

                s3_f.upload(file_path, file_key)

                upload_list.append(s3_f.key) if s3_f.key else None

        self.folder_list = upload_list if len(upload_list) else None

        return self

    def list_dir(self, folder_key):
        """Method for getting all the keys in a specific folder/bucket in S3
        Args:
            folder_key (str): key to desired folder to be listed
        returns:
            list of keys that are listed in the 'folder'
        """
        self.folder_list = list(self.bucket.list(folder_key))
        return self.folder_list


def s3_file(bucket, key):
    """Method for handling the context of the relevant class method, handles errors from the class
    object and attaches them to the returned objects properties if they happen
    Args:
        bucket (str): S3 bucket to work from
        key (str): S3 key for asset
    Returns:
        S3File Class  object
    """

    try:
        s3_f = S3File(bucket, key)
        s3_f.error = False
        return s3_f
    except S3ResponseError as e:
        log.critical('S3 Response Error: {} - Bucket: {} Key: {}'.format(e.message, bucket, key))
        s3_file.error = True
        s3_file.message = e.message
        return s3_file


def s3_folder(bucket, key):
    """Method for handling the context of the relevant class method, handles errors from the class
    object and attaches them to the returned objects properties if they happen
    Args:
        bucket (str): S3 bucket to work from
        key (str): S3 key for asset
    Returns:
        S3Folder Class  object
    """
    try:
        s3_f = S3Folder(bucket, key)
        s3_f.error = False
        return s3_f
    except S3ResponseError as e:
        log.critical('S3 Response Error: {} - Bucket: {} Key: {}'.format(e.message, bucket, key))
        s3_folder.error = True
        s3_folder.message = e.message
        return s3_folder