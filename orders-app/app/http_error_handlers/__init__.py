from flask import Blueprint

from app import http_response as http, db


error_handlers = Blueprint('error_handlers', __name__)


@error_handlers.app_errorhandler(400)
def bad_request(*args, **kwargs):
    return http.http_400({'error': "Bad request. Your request might be malformed"})


@error_handlers.app_errorhandler(401)
def unauthorised_error(*args, **kwargs):
    return http.http_401()


@error_handlers.app_errorhandler(404)
def not_found(*args, **kwargs):
    return http.http_404()


@error_handlers.app_errorhandler(405)
def unsupported_method(*args, **kwargs):
    return http.http_405()


@error_handlers.app_errorhandler(500)
def server_error(*args, **kwargs):
    db.session.rollback()
    return http.create_response({'error': 'Sorry. An error occurred on our end'}, 500)
