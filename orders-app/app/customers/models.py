from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.utils.db import DbSessionModel


class Customer(db.Model, DbSessionModel):
    __tablename__ = 'customers'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    full_name = db.Column(db.String(64), nullable=False, index=True)
    phone = db.Column(db.String(16), nullable=True)
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    password_hash = db.Column(db.String(300))

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, raw_password):
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            'code': self.id,
            'email': self.email,
            'full_name': self.full_name,
            'phone': self.phone,
            'date_joined': self.date_joined.strftime('%y-%m-%d')
        }
