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
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.create_bucket(Bucket='test_bucket')

        # Call the function with the mock parameters
        upload_file_to_s3(s3, 'test_bucket', 'test_key')

        # Check if the file was created and contents are correct
        response = s3.get_object(Bucket='test_bucket', Key='test_key')
        data = response['Body'].read().decode('utf-8')
        #body = s3.Object('test_bucket', 'hello_world.txt').get()['Body'].read().decode("utf-8")
        self.assertEqual(data, "Hello World")

        # Cleanup: delete created file
        if os.path.exists("hello_world.txt"):
            os.remove("hello_world.txt")

if __name__ == '__main__':
    unittest.main()
