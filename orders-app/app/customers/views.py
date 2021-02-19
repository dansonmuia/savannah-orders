from flask import g

from app import http_response as http
from app.auth import decorators as decs

from . import customers, forms as f, models as m


@customers.route('/', methods=['POST'])
def customer_signup():
    form = f.CustomerForm()
    if form.validate():
        customer = form.create_customer()
        customer.save()
        return http.http_201(customer.to_json())

    return http.form_errors(form)


@customers.route('/<email>')
@decs.require_login
def view_customer_details(email):
    customer = m.Customer.query.filter_by(email=email).first_or_404()
    if g.user == customer:
        return http.http_200(customer.to_json())

    return http.http_404()
