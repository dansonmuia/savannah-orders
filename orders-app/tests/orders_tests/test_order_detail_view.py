from tests import http_functions as http, url_map


class TestOrderDetailView:
    def test_customer_can_view_order_details(self, customer, client, order):
        response, rv = http.get(client, url_map.order_detail(order), login_with=customer)

        assert response.status_code == 200
        assert rv['id'] == order.id
        assert rv['amount'] == order.amount
        assert rv['item'] == order.item
        assert rv['time_placed'] is not None
        assert rv['customer_email'] == order.customer.email

    def test_non_logged_in_users_cannot_view_order_detail(self, client, order):
        response, rv = http.get(client, url_map.order_detail(order))

        assert response.status_code == 401
