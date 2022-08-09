import boto3

dynamo_client = boto3.client('dynamodb')

def get_user_accounts():
    return dynamo_client.scan(
        TableName='userCreation'
    )