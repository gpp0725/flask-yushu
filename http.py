# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 0001 22:21
# @Author   : Gpp
# @File     : http.py
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
