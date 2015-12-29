# -*- coding: utf8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:wrk#%%^lsf@127.0.0.1/lcy"
db = SQLAlchemy(app)
app.config['WTF_CSRF_ENABLED'] = False

from .views.myrestful import bp_users

app.register_blueprint(bp_users)

from .views.myrestless import manager
from .views.mypluggableviews import *
