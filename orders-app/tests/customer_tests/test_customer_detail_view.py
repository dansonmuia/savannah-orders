from tests import url_map, http_functions as http


class TestUserDetailView:
    def test_user_can_view_own_detail(self, customer, client):
        response, rv = http.get(client, url_map.customer_detail(customer), login_with=customer)

        assert response.status_code == 200

        assert rv['email'] == customer.email
