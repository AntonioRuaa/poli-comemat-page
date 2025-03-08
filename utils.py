import boto3
from botocore.exceptions import ClientError

def bucket_exists(bucket_name: str) -> bool:
    s3 = boto3.client("s3")
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            return False
        raise e


def dynamo_table_exists(table_name: str) -> bool:
    dynamodb = boto3.client("dynamodb")
    try:
        response = dynamodb.describe_table(TableName=table_name)
        if response.get("Table", {}).get("TableStatus") == "ACTIVE":
            return True
        return False
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            return False
        raise e