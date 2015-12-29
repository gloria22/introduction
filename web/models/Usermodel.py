# -*- coding: utf8 -*-

from .. import db
from sqlalchemy import *


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
