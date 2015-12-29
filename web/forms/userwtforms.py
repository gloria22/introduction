# -*- coding: utf8 -*-
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from ..models.Usermodel import User


class UserForm(Form):
    name = StringField(u'用户名', validators=[DataRequired(), Length(min=4)])

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        if User.query.filter(User.name == self.name.data).scalar():
            self.name.errors.append({'status': 400, 'message': 'duplicate name'})
            return False
        return True
