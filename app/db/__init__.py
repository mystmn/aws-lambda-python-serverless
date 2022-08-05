from flask import Flask
from flask_dynamo import Dynamo

app = Flask(__name__)
app.config['DYNAMO_TABLES'] = [
{
        'TableName' : 'userCreation',
        'KeySchema' : [
                dict(AttributeName='userEmail', KeyType='HASH'),
                dict(AttributeName='userPassword', KeyType='RANGE')
        ],
        'AttributeDefinitions' : [
                dict(AttributeName='username', AttributeType='S'),
                dict(AttributeName='userPassword', AttributeType='S')
        ],
        'ProvisionedThroughput' : 
                dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
        }    
]
 
dynamo = Dynamo(app)