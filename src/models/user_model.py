# -------------------------------------
# Plan It
# Web Service
# 'user_model.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from marshmallow import Schema, fields, post_load
import datetime as dt

class User():

    def __init__(self, user_id: str, username: str, email: str, password: str):

        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.created_time = str(dt.datetime.now())

class UserSchema(Schema):

    user_id = fields.Str()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    created_time = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
