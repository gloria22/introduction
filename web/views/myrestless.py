# -*- coding: utf8 -*-
from flask_restless import APIManager, ProcessingException
from .. import app, db
from ..models.Computermodel import Computer
from flask import request


def req_check(*args, **kwargs):
    if request.path.split("/")[-1].encode('utf-8').isdigit():
        raise ProcessingException(description="get single", code=400)
    else:
        pass


manager = APIManager(app=app, flask_sqlalchemy_db=db, preprocessors=dict(GET_SINGLE=[req_check], GET_MANY=[req_check]))
manager.create_api(Computer, methods=['GET', 'POST', 'DELETE', 'PUT'])
