# -*- coding: utf8 -*-
from .. import db
from sqlalchemy import *


class Computer(db.Model):
    __tablename__ = 'computer'
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
