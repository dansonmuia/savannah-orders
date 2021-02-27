''' Application's url map '''


LOGIN = '/login'
SIGNUP = '/customers'
LIST_ORDERS = '/orders'


def customer_detail(customer):
    return f'/customers/{customer.email}'


def order_detail(order):
    return f'/orders/{order.id}'
