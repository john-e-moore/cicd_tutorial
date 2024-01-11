import boto3
import os

def upload_file_to_s3(s3, bucket, key):
    # String to write to the file
    content = "Hello World"

    # Writing the string content to a file
    with open("hello_world.txt", "w") as file:
        file.write(content)

    # Upload the file
    s3.upload_file("hello_world.txt", bucket, key)

environment = os.getenv('CICD_TUTORIAL_ENVIRONMENT')
print(environment)
# Create an S3 client
s3 = boto3.client('s3')
# Replace 'your_bucket_name' and 'your_key' with your S3 bucket name and desired key
upload_file_to_s3(s3, 'mushroomsundays', f'cicd_tutorial/{environment}/hello_world.txt')
