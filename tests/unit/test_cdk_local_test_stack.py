import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_local_test.cdk_local_test_stack import CdkLocalTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_local_test/cdk_local_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLocalTestStack(app, "cdk-local-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
