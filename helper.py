# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 0001 22:24
# @Author   : Gpp
# @File     : helper.py

def is_isbn_or_key(word):
    # isbn 判断
    # 1. isbn13 由13个0到9的数字组成
    # 2. isbn10 10个0到9的数字组成，含有一‘-’
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigist:
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigist:
        isbn_or_key = 'isbn'
    return isbn_or_key
