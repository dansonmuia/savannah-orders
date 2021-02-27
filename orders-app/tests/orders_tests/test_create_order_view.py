from tests import http_functions as http, url_map


class TestCreateOrderView:
    def test_customer_can_place_order(self, customer, order_data, client):
        response, rv = http.post(client, url_map.LIST_ORDERS, order_data, login_with=customer)

        assert response.status_code == 201
        assert rv['time_placed'] is not None
        assert rv['customer_email'] == customer.email
        assert rv['id'] is not None
        assert rv['item'] == order_data['item']
        assert rv['amount'] == order_data['amount']

    def test_non_logged_in_users_cannot_place_orders(self, order_data, client):
        response, rv = http.post(client, url_map.LIST_ORDERS, order_data)

        assert response.status_code == 401
