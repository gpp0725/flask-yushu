# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 0002 14:24
# @Author   : Gpp
# @File     : book.py
from flask import Flask, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<q><page>')
def search(q, page):
    """
        q : 普通关键字或者isbn
        page
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
        # dict 序列化
        # API
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
