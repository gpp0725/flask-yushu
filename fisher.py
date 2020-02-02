# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 0001 22:21
# @Author   : Gpp
# @File     : http.py
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=81)
