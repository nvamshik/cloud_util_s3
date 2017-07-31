import boto3

def main():



 """   s3_upload("C:/Users/vamshi/Desktop/wordpress.txt")
   s3_bucket("cc-sample-bucket")
   s3_key("wordpress.txt")

def s3_upload(template_file):
    f = open(template_file)
    template_file = f.read()

def s3_bucket(bucket_name):
    with open(bucket_name) as v:
        bucket = v.read()

def s3_key(key_name):
    with open(key_name) as r:
        bucket = r.read()"""

s3_client = boto3.client("s3")
s3_client.upload_file("C:/Users/vamshi/Desktop/wordpress.txt", "cc-sample-bucket", "wordpress.txt")

if __name__ == "__main__":
    main()