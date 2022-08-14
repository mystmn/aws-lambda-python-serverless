import random
import secrets
import string
from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

from app.contoller import aws_controller
# from . import db

profileAccount = Blueprint('profileAccount', __name__)

@profileAccount.route('/scan-user')
def confirm_user_accounts():
    return jsonify(aws_controller.get_user_accounts())

@profileAccount.route('/create-user', methods=[ 'GET', 'POST'])
def create_user_account():
    email = "{}@yahoo.com".format(''.join(random.choices(string.ascii_lowercase, k=5)))
    password = "{}".format(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7)))
    response = aws_controller.controller_create_user_account(email,password )

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