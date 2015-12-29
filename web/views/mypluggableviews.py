# -*- coding: utf8 -*-
from .. import app
from flask.views import MethodView
from ..models.Usermodel import User


@app.route('/showuser/')
def show_users():
    users = User.query.all()
    return "function view"


class ShowUsers(MethodView):
    def get(self):
        users = User.query.all()
        return "method view"


app.add_url_rule('/views/', view_func=ShowUsers.as_view('show users'))
