''' Application's url map '''


LOGIN = '/login'
SIGNUP = '/customers'


def customer_detail(customer):
    return f'/customers/{customer.email}'
