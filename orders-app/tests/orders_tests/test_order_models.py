''' Tests for order models '''
from app.orders.models import Order


class TestOrderModel:
    def test_model_saves_data(self, customer, order_data):
        # Db should be empty at first
        assert Order.query.count() == 0

        order = Order(**order_data, customer=customer)
        order.save()

        assert order.customer_id == customer.id
        assert order.item == order_data['item']
        assert order.amount == order_data['amount']
        assert order.time_placed is not None

