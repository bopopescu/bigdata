# config=utf-8

from flask_login import UserMixin
from common import db

class User(db.Model,UserMixin):
    user_id = db.Column('user_id',db.Integer,primary_key=True)
    accountNumber = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(50),unique=True)

    __tablename__='data_user'

    def __init__(self,user_id=None,accountNumber=None,password=None,name="anonymous"):
        self.user_id = user_id
        self.accountNumber = accountNumber
        self.password = password

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.user_id)
    def __repr__(self):
        return '<User %r>' %(self.accountNumber)
