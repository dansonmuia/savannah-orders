from tests import url_map, http_functions as http


class TestCustomerSignup:
    def test_customer_can_signup(self, client, customer_data):

        response, rv = http.post(client, url_map.SIGNUP, customer_data)

        assert response.status_code == 201

        assert rv['code'] is not None
        assert rv['email'] == customer_data['email']
        assert rv['phone'] == customer_data['phone']
        assert rv['full_name'] == customer_data['full_name']

    def test_user_cannot_duplicate_email(self, client, customer, customer_data):
        assert customer.email == customer_data['email']

        response, rv = http.post(client, url_map.SIGNUP, customer_data)

        assert response.status_code == 400
