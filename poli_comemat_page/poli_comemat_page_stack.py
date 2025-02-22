
from aws_cdk import (
    # Duration,
    Stack, aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct

class PoliComematPageStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "MyBucket",
            bucket_name="my-unique-bucket-name", # specify a unique bucket name
            versioned=True, # enable versioning for the bucket
            encryption=s3.BucketEncryption.S3_MANAGED # use S3-managed encryption
        )
        # example resource
        # queue = sqs.Queue(
        #     self, "PoliComematPageQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
