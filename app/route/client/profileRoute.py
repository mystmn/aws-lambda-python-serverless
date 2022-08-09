from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

from app.contoller import aws_controller
# from . import db

profileAccount = Blueprint('profileAccount', __name__)

@profileAccount.route('/scan-user')
def confirm_user_accounts():
    return jsonify(aws_controller.get_user_accounts())

@profileAccount.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
