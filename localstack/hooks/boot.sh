#!/bin/sh

echo "Running localstack boot script"

# Python版 CDKのインストール
cd /opt/code/localstack/cdk
pip install -r requirements.txt
