# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/12 0012 19:30
# @Author   : Gpp
# @File     : gift.py
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
