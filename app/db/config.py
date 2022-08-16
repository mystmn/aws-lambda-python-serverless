import app

AWS_ACCESS_KEY_ID = "";
AWS_SECRET_ACCESS_KEY ="";

AWS_REGION ='us-east-1'

app.app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
