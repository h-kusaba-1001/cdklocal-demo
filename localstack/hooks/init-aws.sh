#!/bin/sh

export AWS_REGION=ap-northeast-1

echo "CDK settings..."
cd /opt/code/localstack/cdk

cdklocal bootstrap 
echo "CDK bootstrap done!!"

cdklocal deploy
echo "CDK deploy done!!"

# awslocal を使用することも可能
awslocal sqs create-queue --queue-name test-queue
