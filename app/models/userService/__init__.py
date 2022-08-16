import boto3
from app.db.config import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY

# Call the service boto3.[SERVICE]
boto3.setup_default_session(region_name=AWS_REGION)

def get_user_accounts():
    return boto3.client('dynamodb').scan(
        TableName='userCreation'
    )

def post_user_account(user, password):
    return  boto3.resource('dynamodb').Table('userCreation').put_item(
        Item={
            'userEmail':user,
            'userPassword':password
        }
    )
