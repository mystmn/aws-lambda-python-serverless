from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

with app.app_context():
    db.init_app(app)
    db.create_all()
    
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     # since the user_id is just the primary key of our user table, use it in the query for the user
#     return User.query.get(int(user_id))

# blueprint for auth routes in our app
from .route.client.loginRoute import loginAccount as loginBluePrint
app.register_blueprint(loginBluePrint)

# blueprint for non-auth parts of app
from .route.client.indexRoute import indexRoute as indexBluePrint
app.register_blueprint(indexBluePrint)

from .route.client.profileRoute import profileAccount as profileBluePrint
app.register_blueprint(profileBluePrint)