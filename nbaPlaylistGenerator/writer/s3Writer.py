import logging

import boto3
from botocore.exceptions import ClientError


class S3Writer:

    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket = bucket_name

    def write_to_s3(self, file_path, object_name):
        try:
            response = self.s3_client.upload_file(file_path, self.bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
