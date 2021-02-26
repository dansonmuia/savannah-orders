from flask import Blueprint

from app.http_response import http_200


welcome = Blueprint('welcome', __name__)


@welcome.route('/')
def welcome_msg():
    return http_200({
        'message': 'People of earth, please find source code and docs here: '
                   'https://github.com/dansonmuia/savannah-orders'
    })
