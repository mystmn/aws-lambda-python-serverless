import boto3
from app.db.config import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY

# Call the service boto3.[SERVICE]
boto3.setup_default_session(region_name=AWS_REGION)
dynamo_client = boto3.client('dynamodb')

def get_user_accounts():
    return dynamo_client.scan(
        TableName='userCreation'
    )