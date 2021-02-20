from wtforms import fields as f, validators as v

from app.utils.forms import JsonForm

from .models import Order


class OrderForm(JsonForm):
    item = f.StringField('Item Name', validators=[v.DataRequired(), v.Length(max=64)])
    amount = f.IntegerField('Amount', validators=[v.DataRequired()])

    def create_order(self, customer):
        order = Order(**self.data, customer=customer)
        order.save()
        return order
