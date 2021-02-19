from wtforms import validators as v, fields as f, ValidationError

from app.utils.forms import JsonForm
from app.customers.models import Customer as User

login_error_msg = 'Invalid email or password'


class LoginForm(JsonForm):
    email = f.StringField('Email', validators=[v.DataRequired(), v.Email()])
    password = f.StringField('Password', validators=[v.DataRequired()])
    user = None

    def validate_email(self, field):
        # Actually validate both email and check password here
        user = User.query.filter_by(email=field.data).first()
        if user is None or not user.check_password(self.password.data):
            raise ValidationError(login_error_msg)
        self.user = user
