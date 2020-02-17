# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/17 0017 13:22
# @Author   : Gpp
# @File     : test_en_de.py
import base64


def base64e(s):
    return str(base64.urlsafe_b64encode(bytes(s, encoding="UTF-8")), encoding="UTF-8")


def base64d(s):
    i = len(s) % 4
    if i == 1:
        s = s + '='
    elif i == 2:
        s = s + '=='
    return str(base64.urlsafe_b64decode(s), encoding="UTF-8")
