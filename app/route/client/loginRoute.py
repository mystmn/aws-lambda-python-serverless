from flask import Blueprint, redirect, render_template, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user

from random import randint

loginAccount = Blueprint('loginAccount', __name__)

@loginAccount.route('/scanUser', methods=[ 'GET', 'POST'])
def create_account():
    userEmailAccount =  (f"{randint(0,50000)}@google.com")
    userPasswordAccount =  "sfsdfsklkjk"

    print(f"User created '{userEmailAccount}' and '{userPasswordAccount}' ")