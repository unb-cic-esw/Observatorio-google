import boto3
import json

s3 = boto3.resource('s3')
bucket = s3.Bucket('timegoogle')

fileName = input()

data = ""
for obj in bucket.objects.all():
	if(obj.key == fileName):
		data = obj.get()['Body'].read().decode('utf8')

print(data)