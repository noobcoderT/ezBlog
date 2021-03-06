#!/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager, login_user, logout_user, current_user, login_required
from flask_login import UserMixin
from flask_blogging import SQLAStorage, BloggingEngine
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sslify import SSLify
import datetime

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(hours=3)
app.config['USE_HTTPS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/ezBlog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "ezBlog"  # for WTF-forms and login
app.config["BLOGGING_URL_PREFIX"] = "/blog"
app.config["BLOGGING_SITEURL"] = "http://traceme.space"
app.config["BLOGGING_AUTHOR"] = "Ziv & Ada"
app.config["BLOGGING_SITENAME"] = "ezBlog"
app.config["FILEUPLOAD_IMG_FOLDER"] = "data/img"  #img will not upload here, i do not know why
app.config["FILEUPLOAD_PREFIX"] = "/fileupd"
app.config["FILEUPLOAD_ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg", "gif", "bmp", "webp"]
app.config["BLOGGING_ALLOW_FILEUPLOAD"] = True
app.config["BLOGGING_LINKS"] = [{"name":"Github","link":"https://github.com/noobcoderT"},
        {"name":"Email","link":"mailto:tangzjxb@gmail.com"}]
app.config["BLOGGING_POSTS_PER_PAGE"] = 8
app.config["BLOGGING_ARCHIVES_PER_PAGE"] = 20

if app.config['USE_HTTPS']:
    sslify = SSLify(app)

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(64), unique=True)
    #posts = blog_db.relationship(, backref = , lazy = ) ## posts blongs to cur user
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def get_name(self):
        return self.username

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)

with app.app_context():

    blog_sql_storage = SQLAStorage(db=db)
    blog_login_manager = LoginManager(app)
    blog_login_manager.session_protection = 'strong'
    blog_login_manager.login_view = 'login'
    blog_login_manager.login_message = 'Please enter your account'
    blog_login_manager.init_app(app)
    db.create_all()

blog_extns = ['markdown.extensions.extra', 'markdown.extensions.codehilite',
                'markdown.extensions.tables','markdown.extensions.toc']
blog_engine = BloggingEngine(app, blog_sql_storage, extensions=blog_extns)

from flask_blogging.sqlastorage import Post, Tag

@blog_login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

@app.route("/")
def index():
    return redirect("/blog/")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    global nxt
    if request.method == 'GET':
        nxt = request.args.get("next", None)
    if current_user.is_authenticated:
        if nxt:
            return redirect(nxt)
        else:
            return redirect('/blog/')
    form = LoginForm()
    if form.validate_on_submit():
        input_username = request.form.get('username', None)
        input_password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        user = User.query.filter_by(username=input_username, password=input_password).first()
        if user is not None:
            login_user(user, remember=remember_me)
            if nxt:
                return redirect(nxt)
            else:
                return redirect('/blog/')
        else:
            flash(u'用户名或密码错误！', 'warning')
    return render_template('blogging/login.html', form=form)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect("/blog/")

if __name__ == "__main__":
    if app.config['USE_HTTPS']:
        app.config["BLOGGING_SITEURL"] = app.config["BLOGGING_SITEURL"].replace('http', 'https')
        context = ('server.crt', 'server.key')
        app.run(debug=True, host='::', port=443, use_reloader=True, ssl_context=context)
    else:
        app.run(debug=True, host='::', port=8888, use_reloader=True)
