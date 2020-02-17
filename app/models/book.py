# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 0005 22:28
# @Author   : Gpp
# @File     : book.py

# sqlalchemy 第三方的python的包
# flask在这个包的基础上封装了Flask_SQLAlchemy，使flask更加人性化
from app.models.base import db

from sqlalchemy import Column, Integer, String


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键本身就不重复，自增长
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未命名')
    binding = Column(String(20))  # 精装还是普装
    publisher = Column(String(20))  # 出版
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)  # unique唯一的
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
