# -*- coding: utf8 -*-
from flask_restless import APIManager
from .. import app, db
from ..models.Computermodel import Computer

manager = APIManager(app=app, flask_sqlalchemy_db=db)
manager.create_api(Computer, methods=['GET', 'POST', 'DELETE', 'PUT'])
