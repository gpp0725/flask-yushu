# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 0002 14:24
# @Author   : Gpp
# @File     : book.py
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

from . import web
from app.forms.book import SearchForm


@web.route('/book/search')
def search(q, page):
    """
        q : 普通关键字或者isbn
        page
    :return:
    """
    #  验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
            # dict 序列化
            # API
        return jsonify(result)
        # return json.dumps(result), 200, {'content-type': 'application/json'}
    else:
        return jsonify(form.errors)
