FROM localstack/localstack:3.5

# localstack v3.5では、node18とpython3.11が入っている
RUN npm install -g aws-cdk aws-cdk-local

ENTRYPOINT ["docker-entrypoint.sh"]
