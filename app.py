#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dotenv import (load_dotenv)
from comemat import (
    ComematDynamoStack,
    ComematBucketStack
)
load_dotenv()

app = cdk.App()

env=cdk.Environment(account=os.getenv('ACCOUNT'), region=os.getenv('AWS_REGION'))

comemat_bucket_stack = ComematBucketStack(
    app, 
    "ComematBucketStack",
    env=env
)

comemat_dynamo_stack = ComematDynamoStack(
    app, 
    "ComematDynamoStack",
    env=env
)

comemat_dynamo_stack.add_dependency(comemat_bucket_stack)

app.synth()
