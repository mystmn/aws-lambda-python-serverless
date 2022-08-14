import random
import secrets
import string
from flask import Blueprint, jsonify
from flask_login import current_user

from ..models import userService

profileController = Blueprint('profileController', __name__)

# Universal
email = "{}@yahoo.com".format(''.join(random.choices(string.ascii_lowercase, k=5)))
password = "{}".format(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7)))
    
# Routes
@profileController.route('/scan-user')
def confirm_user_accounts():
    return jsonify(userService.get_user_accounts())

@profileController.route('/create-user', methods=[ 'GET', 'POST'])
def create_user_account():
    response = userService.post_user_account(email,password )

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
       return {
           'msg': 'Add Movie successful',
           'email': email,
           'password': password
       }
    return { 
       'msg': 'error occurred',
       'response': response
    }