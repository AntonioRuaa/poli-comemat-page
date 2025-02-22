import aws_cdk as core
import aws_cdk.assertions as assertions

from poli_comemat_page.poli_comemat_page_stack import PoliComematPageStack

# example tests. To run these tests, uncomment this file along with the example
# resource in poli_comemat_page/poli_comemat_page_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PoliComematPageStack(app, "poli-comemat-page")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
