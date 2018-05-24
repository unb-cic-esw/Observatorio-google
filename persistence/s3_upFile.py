import boto3
import os
# Create an S3 client
s3 = boto3.client('s3')

filename = input()
bucket_name = os.environ['S3_BUCKET']

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)
