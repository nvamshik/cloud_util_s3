import boto3

s3_resource = boto3.resource('s3')
for bucket in s3_resource.buckets.all():
    print(bucket.name)

with open('filename', 'rb') as data:
    s3_resource.upload_fileobj(data, 'mycalibucket', 'mykey')