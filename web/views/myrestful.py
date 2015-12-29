# -*- coding: utf8 -*-
from flask import Blueprint
from flask import jsonify
from flask_restful import Resource, Api

from .. import db
from ..forms.userwtforms import UserForm
from ..models.Usermodel import User


class Something(Resource):
    def get(self, id=None):
        if not id:
            user = User.query.all()
            result = [{'id': u.id, 'name': u.name} for u in user]
        else:
            user = User.query.get_or_404(id)
            result = [{'id': user.id, 'name': user.name}]
        return jsonify(result=result)

    def post(self):
        form = UserForm()
        if form.validate_on_submit():
            user = User(name=form.name.data)
            db.session.add(user)
            db.session.commit()
            return 'post success', 201
        else:
            if form.name.errors:
                return 'name error', 400

    def put(self, id):
        user = User.query.get_or_404(id)
        form = UserForm()
        if form.validate_on_submit():
            user.name = form.name.data
            db.session.commit()
            return 'put success', 201
        else:
            if form.name.errors:
                return 'name error', 400

    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return 'no user', 404
        db.session.delete(user)
        db.session.commit()
        return 'delete success', 204


bp_users = Blueprint('myuser', __name__, url_prefix='/user')
api_users = Api(bp_users)
api_users.add_resource(Something, '/<int:id>', endpoint='User1', methods=['GET', 'PUT', 'DELETE'])
api_users.add_resource(Something, '/', endpoint='User2', methods=['GET', 'POST'])
