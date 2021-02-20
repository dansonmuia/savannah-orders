from flask import g

from app import http_response as http
from app.auth import decorators as decs

from . import orders, forms as f


@orders.route('/', methods=['POST'])
@decs.require_login
def create_order():
    form = f.OrderForm()
    if form.validate():
        order = form.create_order(customer=g.user)
        return http.http_201(order.to_json())
    return http.form_errors(form)
