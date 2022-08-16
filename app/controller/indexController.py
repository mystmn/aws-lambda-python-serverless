from re import template
from flask import Blueprint, render_template

indexController = Blueprint('indexController', __name__)

@indexController.route('/')
def index():
    return render_template('index.html', menu=menu(), title=index.__name__)


def menu():
    return {'Home': '/', 'About': '/about'}