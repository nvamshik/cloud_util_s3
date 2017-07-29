import boto3

def main():
    s3_upload("C:/Users/vamshi/Desktop/Vamshi_WordPress.txt")

def s3_upload(template_file):
    with open(template_file) as f:
        template = f.read()

def s3_bucket(bucket_name):
    with open(bucket_name) as v:
        bucket = v.read()

def s3_file(file_name):
    with open(file_name) as b:
        uploadfilename = b.read()

    s3_client = boto3.client("s3")
    s3_client.upload_file(template_file, bucket_name, file_name)

if __name__ == "__main__":
    main()