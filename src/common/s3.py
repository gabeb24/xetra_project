"""Connector and methods that access S3 buckets"""

import os
import boto3

class S3BucketConnector():
    """
    Class for interacting with S3 buckets
    """

    def __init__(self, access_key: str, secret_access_key: str):