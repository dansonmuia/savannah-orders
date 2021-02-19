from app import http_response as http

from . import auth
from .forms import LoginForm
from .tokens import generate_access_token


@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate():
        user = form.user
        return http.http_200({'message': 'Access token generated successfully',
                              'access_token': generate_access_token(user)})

    return http.form_errors(form)
