from wtforms import fields as f, validators as v, ValidationError

from app.utils.forms import JsonForm

from .models import Customer


class CustomerForm(JsonForm):
    email = f.StringField('Email', validators=[v.Email(), v.Length(max=50), v.DataRequired()])
    full_name = f.StringField('Full name', validators=[v.Length(min=3, max=50), v.DataRequired()])
    phone = f.StringField('Phone number', validators=[v.Length(max=16, min=9)])
    password = f.StringField('Password', validators=[v.DataRequired()])

    def validate_email(self, field):
        if Customer.query.filter_by(email=field.data).first() is not None:
            raise ValidationError('This email is not available')

    def create_customer(self):
        customer = Customer(
            email=self.email.data,
            full_name=self.full_name.data,
            phone=self.phone.data,
            password=self.password.data)
        return customer
