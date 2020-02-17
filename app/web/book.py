# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 0002 14:24
# @Author   : Gpp
# @File     : book.py
from flask import jsonify, request, render_template, flash
import json
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

from . import web
from app.forms.book import SearchForm
from ..view_models.book import BookCollection, BookViewModel


@web.route('/book/search')
def search():
    """
        q : 普通关键字或者isbn
        page
    :return:
    """
    #  验证层
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)

        else:
            yushu_book.search_by_keyword(q, page)
            # dict 序列化
            # API
        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__), 200, {'content-type': 'application/json'}
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': 'gpp',
        'age': 18
    }
    flash('hello,pp', category='erro')
    flash('hello,sz', category='warning')
    return render_template('test.html', data=r)

