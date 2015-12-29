# -*- coding: utf8 -*-
from ..models.Personmodel import Person
from wtforms_alchemy import ModelForm


class Person_Form(ModelForm):
    class Meta:
        model = Person
