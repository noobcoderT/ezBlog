#!/bin/env python
# -*- coding: utf-8 -*-

from ezBlog import User, db
import sys

def create_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
    else:
        if user.password != password:
            user.password = password
            db.session.add(user)
            db.session.commit()

def delete_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user is not None:
        db.session.delete(user)
        db.session.commit()

if __name__ == '__main__':

    command = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    if command == 'create':
        create_user(username, password)
    elif command == 'delete':
        delete_user(username, password)
    else:
        pass
