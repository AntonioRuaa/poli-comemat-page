
from aws_cdk import (
    # Duration,
    Stack, aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct
from utils import bucket_exists
import os

class ComematBucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        if not bucket_exists(os.getenv("IMAGES_BUCKET")):

            images_bucket = s3.Bucket(self, "ImagesBucket",
                bucket_name=os.getenv("IMAGES_BUCKET"), # specify a unique bucket name
                versioned=False, # enable versioning for the bucket
                encryption=s3.BucketEncryption.S3_MANAGED # use S3-managed encryption
            )

        else:
            images_bucket = s3.Bucket.from_bucket_name(
                self, 
                "ImagesBucket",
                bucket_name=os.getenv("IMAGES_BUCKET"),
            )
