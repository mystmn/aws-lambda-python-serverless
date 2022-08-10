import app

# AWS_ACCESS_KEY_ID = 'AKIAWBZSFYUGW3ENUZNF'
AWS_ACCESS_KEY_ID = 'AKIAWBZSFYUGXAYLN44C'
# AWS_SECRET_ACCESS_KEY = '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'
AWS_SECRET_ACCESS_KEY = 'Mve02M4XY4f/F1ynicv10QNHHoaTL1s543SnEu1N'

AWS_REGION ='us-east-1'

app.app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
