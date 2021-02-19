from app import http_response as http

from . import customers, forms as f


@customers.route('/', methods=['POST'])
def customer_signup():
    form = f.CustomerForm()
    if form.validate():
        customer = form.create_customer()
        customer.save()
        return http.http_201(customer.to_json())

    return http.form_errors(form)
