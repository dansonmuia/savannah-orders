from flask import g

from app import http_response as http
from app.auth import decorators as decs
from app.utils import pagination

from . import orders, forms as f, models as m


@orders.route('/', methods=['POST'])
@decs.require_login
def create_order():
    form = f.OrderForm()
    if form.validate():
        order = form.create_order(customer=g.user)
        return http.http_201(order.to_json())
    return http.form_errors(form)


@orders.route('/', methods=['GET'])
@decs.require_login
def list_orders():
    '''
    :return:

    Returns a list of the orders placed by the logged in customer
    '''

    orders_query = m.get_orders_query(g.user)

    return pagination.jsonify_pagination(pagination.paginate(orders_query))
