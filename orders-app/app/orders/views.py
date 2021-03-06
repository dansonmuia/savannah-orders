from flask import g

from app import http_response as http
from app.auth import decorators as decs
from app.utils import pagination
from app.sms.sms import send_confirm_order_sms

from . import orders, forms as f, models as m


@orders.route('/', methods=['POST'])
@decs.require_login
def create_order():
    form = f.OrderForm()
    if form.validate():
        order = form.create_order(customer=g.user)
        send_confirm_order_sms(order)
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


@orders.route('/<order_id>', methods=['GET'])
@decs.require_login
def get_order_detail(order_id):
    order = m.get_orders_query(g.user).filter_by(id=order_id).first_or_404()
    return http.http_200(order.to_json())
