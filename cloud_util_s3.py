import boto3
import os
import logging

logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"
)


def main():
  s3_upload("C:/Users/vamshi/Desktop/wordpress.txt","cc-sample-bucket","test333.txt")
  file_validation("C:/Users/vamshi/Desktop/wordpress.txt")


def file_validation(path):
    status = os.path.isfile(path)
    logging.debug(status)


def s3_upload(template_file, bucket_name, key_name):
    s3_client.upload_file(template_file, bucket_name, key_name)


s3_client = boto3.client("s3")

if __name__ == "__main__":
    main()
