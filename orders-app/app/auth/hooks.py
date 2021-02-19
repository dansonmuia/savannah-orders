from flask import request, g

from . import auth
from .tokens import load_user_from_access_token


@auth.before_app_request
def get_user():
    user = None
    try:
        access_token = request.headers.get('Authorization', '')
        user = load_user_from_access_token(access_token)
    except Exception:
        pass

    g.user = user
