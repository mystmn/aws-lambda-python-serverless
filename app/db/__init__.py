from app import app
from flask_dynamo import Dynamo

def dynamoDBConnection():
    app.config['DYNAMO_TABLES'] = [{
            TableName='userCreation',
            KeySchema=[dict(AttributeName='userEmail', KeyType='HASH')],
            AttributeDefinitions=[dict(AttributeName='userEmail', AttributeType='S')],
            ProvisionedThroughput=dict(ReadCapacityUnits=1, WriteCapacityUnits=1)
    }]

    dynamo = Dynamo()
    dynamo.init_app(app)
    return app