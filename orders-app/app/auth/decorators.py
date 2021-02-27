from functools import wraps

from flask import g

from app.http_response import http_401


def require_login(fn):
    @wraps(fn)
    def require_login_decorator(*args, **kwargs):
        if g.user is None:
            return http_401()
        return fn(*args, **kwargs)
    return require_login_decorator
