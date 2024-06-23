from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
)
from constructs import Construct

class CdkLocalTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sqs.Queue(
            self, "TestQueue1",
            visibility_timeout=Duration.seconds(300),
        )

        s3.Bucket(self,
            "TestBucket",
            bucket_name='test-bucket',
        )


