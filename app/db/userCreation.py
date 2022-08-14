import boto3

def create_user_table(dynamoDB=None):
        dynamoDB = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

        table = dynamoDB.create_table(
                TableName='userCreation',
                KeySchema=[
                        {
                                'AttributeName': 'userEmail',
                                'KeyType': 'HASH'  # Partition key
                        },
                        {
                                'AttributeName': 'userPassword',
                                'KeyType': 'RANGE'  # Sort key
                        }
                        ],
                        AttributeDefinitions=[
                        {
                                'AttributeName': 'userEmail',
                                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                                'AttributeType': 'S'
                        },
                        {
                                'AttributeName': 'userPassword',
                                'AttributeType': 'N'
                        },
                ],
                ProvisionedThroughput={
                        # ReadCapacityUnits set to 10 strongly consistent reads per second
                        'ReadCapacityUnits': 2,
                        'WriteCapacityUnits': 2  # WriteCapacityUnits set to 10 writes per second
                }
        )
        return table