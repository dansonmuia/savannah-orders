import random

import pytest
from faker import Faker

from app import create_app, db
from app.customers.models import Customer
from app.orders.models import Order


@pytest.fixture(scope='session')
def session_app():
    app = create_app('config.TestConfig')
    return app


@pytest.fixture(autouse=True)
def app(session_app):
    context = session_app.app_context()
    context.push()
    db.create_all()

    yield session_app

    db.session.remove()
    db.drop_all()
    context.pop()


@pytest.fixture()
def client(app):
    return app.test_client()


faker = Faker()


@pytest.fixture()
def customer_data():
    return {'email': faker.email(),
            'full_name': faker.name(),
            'phone': faker.msisdn(),
            'password': faker.password(),
            }


def save_customer(customer_data):
    customer = Customer(**customer_data)
    customer.save()
    return customer


@pytest.fixture()
def customer_with_password(customer_data):
    password = customer_data['password']
    customer = save_customer(customer_data)
    return customer, password


@pytest.fixture()
def customer(customer_with_password):
    _customer, password = customer_with_password
    return _customer


@pytest.fixture()
def order_data():
    return {
        'item': faker.name(),
        'amount': random.randint(1, 999999)
    }


@pytest.fixture()
def order(order_data, customer):
    _order = Order(**order_data, customer=customer)
    _order.save()
    return _order
