# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 0002 14:23
# @Author   : Gpp
# @File     : __init__.py.py
from flask import Flask
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from app.models.base import db
from app.models.user import User

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.settings')
    app.config.from_object('app.secure')
    register_blueprint(app)
    db.init_app(app)
    login_manager.init_app(app)
    db.create_all(app=app)
    return app


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
