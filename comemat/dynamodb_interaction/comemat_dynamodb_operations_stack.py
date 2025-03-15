from aws_cdk import (
    aws_dynamodb as dynamodb,
    Stack,
    CfnOutput
)
from constructs import Construct
from utils import dynamo_table_exists
import os


class ComematDynamoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        if not dynamo_table_exists(os.getenv("CONTENT_DYNAMO_TABLE")):
            content_table = dynamodb.Table(
                self,
                "ContentTable",
                table_name=os.getenv("CONTENT_DYNAMO_TABLE"),
                partition_key=dynamodb.Attribute(
                    name="content_type", type=dynamodb.AttributeType.STRING
                ),
                sort_key=dynamodb.Attribute(
                    name="tittle", type=dynamodb.AttributeType.STRING
                ),
                billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
                encryption=dynamodb.TableEncryption.AWS_MANAGED,
            )
        else:
            content_table = dynamodb.Table.from_table_name(
                self,
                "ContentTable",
                table_name=os.getenv("CONTENT_DYNAMO_TABLE"),
            )

        #CfnOutput(
            #self, 
            #"ContentTable", 
            #value=content_table.table_name,
            #export_name="ContentTable"
        #)
