# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 0002 23:13
# @Author   : Gpp
# @File     : user.py
from . import web

@web.route('/login')
def login():
    return 'login'
