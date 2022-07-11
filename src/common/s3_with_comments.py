"""Connector and methods that access S3 buckets"""

import logging
import os
import boto3


class S3BucketConnector():
    """
    Class for interacting with S3 buckets
    """

    def __init__(self, access_key: str, secret_access_key: str, endpoint_url: str, bucket: str):
        """
        Constructor for S3 Bucket Connector
        :param access_key: access key to access S3
        :param secret_key: secret key for accessing S3
        :param endpoint_url: endpoint url to S3
        "param bucket: S3 bucket name
        """
        self._logger = logging.getLogger(__name__)
        self.endpoint_url = endpoint_url
         # using OS package to access our environmental variables
        self.session = boto3.Session(aws_access_key_id=os.environ[access_key],
                                    aws_secret_access_key=os.environ[secret_access_key])

       # protecting the variables. Other developers would not touch these variables.
       # if they were __ they would be private
        self._s3 = self.session.resource(service_name='s3',
        endpoint_url=endpoint_url)
        self._bucket = self._s3.Bucket(bucket)
# Class Methods
    def list_files_in_prefix(self, prefix: str):
        """
        listing all files with a prefix on the S3 bucket

        :param prefix: prefix on the S3 bucket that should be filtered with

        returns:
            files: list of all file names containing the prefix in the key
        """
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)]
        return files

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass
