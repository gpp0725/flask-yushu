# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/3 0003 11:06
# @Author   : Gpp
# @File     : book.py
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
