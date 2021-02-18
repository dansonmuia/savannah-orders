# Test customer model functionality

import pytest

from sqlalchemy.exc import IntegrityError

from app.customers.models import Customer


class TestCustomerModel:
    def test_model_saves_user_data(self, customer_data):
        # DB should be empty
        assert Customer.query.count() == 0

        # Create one user
        customer = Customer(**customer_data)
        customer.save()

        assert customer.id is not None
        assert Customer.query.count() == 1

    def test_set_and_verify_password(self, customer_data):
        customer = Customer(**customer_data)
        customer.save()

        assert customer.password != customer_data['password']
        assert customer.check_password(customer_data['password']) is True

    def test_cannot_duplicate_email(self, customer, customer_data):
        # Customer data with duplicate email
        data = {**customer_data, 'email': customer.email}

        with pytest.raises(IntegrityError):
            customer2 = Customer(**data)
            customer2.save()
