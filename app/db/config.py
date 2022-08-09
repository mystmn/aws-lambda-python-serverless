from ...app import app

AWS_ACCESS_KEY_ID='AKIAWBZSFYUGW3ENUZNF'
AWS_SECRET_ACCESS_KEY='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'
REGION_NAME='us-east-1'

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'y
