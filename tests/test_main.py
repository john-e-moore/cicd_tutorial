import unittest
from moto import mock_s3
import boto3
import os
from src.main import upload_file_to_s3

class TestS3Upload(unittest.TestCase):

    @mock_s3
    def test_upload_file_to_s3(self):
        # Set up the mock environment
        # Can only use us-east-1 for mock
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='test_bucket')

        # Call the function with the mock parameters
        upload_file_to_s3('test_bucket', 'test_key')

        # Check if the file was created and contents are correct
        body = conn.Object('test_bucket', 'test_key').get()['Body'].read().decode("utf-8")
        self.assertEqual(body, "Hello World")

        # Cleanup: delete created file
        if os.path.exists("hello_world.txt"):
            os.remove("hello_world.txt")

if __name__ == '__main__':
    unittest.main()
