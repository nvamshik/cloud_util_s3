import boto3

def main():
    s3_upload("C:/Users/vamshi/Desktop/wordpress.txt")

def s3_upload(template_file):
    with open(template_file) as f:
        template = f.read()

    s3_client = boto3.client("s3")
    s3_client.upload_file(template_file,"cc-sample-bucket","wordpress.txt")

if __name__ == "__main__":
    main()