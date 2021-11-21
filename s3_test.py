import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.resource('s3')
    s3_bucket = s3_client.Bucket(bucket)
    # key = s3_bucket.objects.all()
    # print(key)
    try:
        response = s3_bucket.download_file(file_name, '/tmp2/download_table_data.json')
    except ClientError as e:
        print(e)
        return False
    return True


bucket_name = 'json-data-storage'
file_name = '/Users/jinyuchen/testbank/table_data2.json'
upload_file(file_name, bucket_name)
