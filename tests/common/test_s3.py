"""TestS3BucketConnectorMethods"""

import os
import unittest
import boto3
from moto import mock_s3

from src.common.s3_with_comments import S3BucketConnector

class TestS3BucketConnectorMethods(unittest.TestCase):
    """
    Testing the S3BucketConnector class
    """
    def setUp(self):
        """
        Setting up the testing environment
        """
        # mocking s3 connection
        self.mock_s3 = mock_s3()
        self.mock_s3.start()
        # defining the class argumetns
        self.s3_access_key = 'AWS_ACCESS_KEY_ID'
        self.s3_secret_key = 'AWS_SECRET_ACCESS_KEY'
        self.s3_endpoint_url = 'https://s3.eu-central-1.amazonaws.com'
        self.s3_bucket_name = 'test-bucket'
        # create S3 access keys as environment variables
        os.environ[self.s3_access_key] = 'KEY1'
        os.environ[self.s3_secret_key] = 'KEY2'
        # CREATING A BUCKET on the mocked s3
        self.s3 = boto3.resource(service_name='s3', endpoint_url=self.s3_endpoint_url)
        self.s3.create_bucket(Bucket=self.s3_bucket_name,
                            CreateBucketConfiguration={
                                'LocationConstraint': 'eu-central-1'
                            })
        self.s3_bucket = self.s3.Bucket(self.s3_bucket_name)
        # creating a testing instance
        self.s3_bucket_conn = S3BucketConnector(self.s3_access_key,
                                                self.s3_secret_key,
                                                self.s3_endpoint_url,
                                                self.s3_bucket_name
                                            )
        print('setUp test running')

    def tearDown(self):
        """
        Executing after unittests, mocking an s3 connection stop
        """
        self.mock_s3.stop()
        print('tearDown test running')

    def test_list_files_in_prefix_ok(self):
        """
        Tests the list_files_in_prefix method for getting 2 file keys
        as list on the mocked s3 bucket
        """
        # Expected test results
        prefix_exp = 'prefix/' # expected prefix
        key1_exp = f'{prefix_exp}test1.csv' 
        key2_exp = f'{prefix_exp}test2.csv'
        # Test init: create csv that can be sed for both files
        csv_content = """col1,col2,
        valA, valB"""
            # putting our expected prefixes that are csv files into an s3 bucket
        self.s3_bucket.put_object(Body=csv_content, Key=key1_exp) 
        self.s3_bucket.put_object(Body=csv_content, Key=key2_exp)
        # method execution
            # use our method on our expected prefix
        list_result = self.s3_bucket_conn.list_files_in_prefix(prefix_exp)
        # tests after method execution
        self.assertEqual(len(list_result), 2) # make sure our result has 2 items
        self.assertIn(key1_exp, list_result) # make sure both keys are in the list
        self.assertIn(key2_exp, list_result)
        print('test_list_files_in_prefix_ok test running')
        # cleanup after tests
        # delete our testing objects
        self.s3_bucket.delete_objects(
            Delete={
                'Objects': [
                    {
                        'Key': key1_exp
                    },
                    {
                        'Key': key2_exp
                    },
                ]
            }

        )
        print("delete_objects test running")

    def test_list_files_in_prefix_wrong_prefix(self):
        """
        Test the list_files_in_prefix method in case of a wrong
        or not existing preifx
        """
       # test init
        prefix = 'no-prefix' # creates an incorrect prefix
        # method execution
        list_result = self.s3_bucket_conn.list_files_in_prefix(prefix)
        self.assertTrue(not list_result) # make sure list_result is empty
        print('test_list_files_in_prefix_wrong_prefix test running')
        

if __name__ == "__main__":
    unittest.main()
    # ways of testing our methods individually to identify bugs:
#    testIns = TestS3BucketConnectorMethods()
#    testIns.setUp()
#    testIns.test_list_files_in_prefix_ok()
#    testIns.tearDown()

   