# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 0001 22:21
# @Author   : Gpp
# @File     : httper.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=81)
