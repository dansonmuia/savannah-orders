from app.auth import tokens


class TestToken:
    def test_access_token(self, customer):
        user = customer
        access_token = tokens.generate_access_token(user)
        loaded_user = tokens.load_user_from_access_token(access_token)

        assert user.id == loaded_user.id
