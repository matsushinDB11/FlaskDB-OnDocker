from flask import Blueprint
hello = Blueprint('hello', __name__, url_prefix='/hello')


@hello.route('/', methods=['GET'])
def hello_index():
    return 'Hello Flask'


@hello.route('/a', methods=['GET'])
def hello_a():
    return 'Hello Flask A'


@hello.route('/matsushin')
def matsushin():
    return 'helo matsushin'
