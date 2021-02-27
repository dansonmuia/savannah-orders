# Test login views

from app.auth.tokens import load_user_from_access_token

from tests import url_map, http_functions as http


class TestLogin:
    def test_login_returns_valid_token(self, customer_with_password, client):
        user, password = customer_with_password

        response, rv = http.post(client, url_map.LOGIN, {'email': user.email, 'password': password})

        assert response.status_code == 200
        assert load_user_from_access_token(rv['access_token']).id == user.id
