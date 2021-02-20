from datetime import datetime

from app import db
from app.utils.db import DbSessionModel


class Order(db.Model, DbSessionModel):
    __tablename__ = 'orders'

    id = db.Column(db.Integer(), primary_key=True)
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'), nullable=False, index=True)
    item = db.Column(db.String(128), nullable=False, index=True)
    amount = db.Column(db.Integer(), nullable=False)
    time_placed = db.Column(db.DateTime(), default=datetime.utcnow)

    def to_json(self):
        return {
            'id': self.id,
            'customer_email': self.customer.email,
            'item': self.item,
            'amount': self.amount,
            'time_placed': self.time_placed.strftime('%y-%m-%d')
        }
