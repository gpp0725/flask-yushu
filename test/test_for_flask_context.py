# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/6 0006 18:56
# @Author   : Gpp
# @File     : test_for_flask_context.py
from flask import Flask, current_app

app = Flask(__name__)
app.config.from_object('app.secure')
ctx = app.app_context()
ctx.push()
# a = current_app
d = current_app.config['DEBUG']
ctx.pop()