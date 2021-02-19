from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask import current_app

from app.customers.models import Customer as User

ACCESS_TOKEN_EXPIRY = 60*60*6


def serializer(expiration):
    return Serializer(current_app.config['SECRET_KEY'], expiration)


def access_token_serializer():
    return serializer(ACCESS_TOKEN_EXPIRY)


def generate_access_token(user):
    token = access_token_serializer().dumps({'scope': 'access', 'email': user.email}).decode('utf-8')

    return f'Bearer {token}'


def load_user(access_token, _serializer, scope):
    try:
        prefix, token = access_token.split(' ')
        if prefix != 'Bearer':
            raise Exception('Invalid token')

        data = _serializer.loads(token.encode('utf-8'))
        email, token_scope = data.get('email'), data.get('scope')
        if token_scope != scope:
            raise BadSignature('Token out of scope')
        return User.query.filter_by(email=email).first()
    except (BadSignature, SignatureExpired):
        return None


def load_user_from_access_token(token):
    _serializer = access_token_serializer()
    return load_user(token, _serializer, 'access')
