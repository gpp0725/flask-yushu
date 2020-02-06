# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 0002 14:23
# @Author   : Gpp
# @File     : __init__.py.py
#  蓝图 blueprint 蓝本
from flask import Blueprint

web = Blueprint('web', __name__)
from app.web import book

