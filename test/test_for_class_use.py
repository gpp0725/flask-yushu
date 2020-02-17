# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/11 0011 19:57
# @Author   : Gpp
# @File     : test_for_class_use.py
class TestUse:
    def __init__(self, book):
        self.author = book['author']
        self.publisher = book['publisher']
        self.price = book['price']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)


class BookColl:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = 0
        self.keyword = keyword
        self.books = [TestUse(book) for book in yushu_book]


yushu_books = [{'author': 'gpp', 'publisher': 'zkr', 'price': '24'}, ]
books = BookColl()
books.fill(yushu_books, 'ha')
for bo in books.books:
    print(bo.intro)
