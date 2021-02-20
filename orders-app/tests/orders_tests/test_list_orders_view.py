from tests import http_functions as http, url_map


class TestListOrdersView:
    def test_customer_can_list_their_orders(self, customer, client, order):
        response, rv = http.get(client, url_map.LIST_ORDERS, login_with=customer)

        assert response.status_code == 200
        assert len(rv['items']) == 1

    def test_non_logged_in_users_cannot_list_customer_orders(self, client, order):
        response, rv = http.get(client, url_map.LIST_ORDERS)

        assert response.status_code == 401
