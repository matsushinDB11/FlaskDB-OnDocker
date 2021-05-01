from flask import Blueprint
index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def index1():
    return 'this is index'
