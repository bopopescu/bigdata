# encoding:utf-8
# !/usr/bin/env python

import json
from flask import render_template,request,redirect,Flask,Blueprint

from flask_login import login_user,login_required

from model.user_model import User
from model.student_info import Student
import pymysql as MySQLdb
from model import login_manager

from form.login_form import LoginForm

userRoute = Blueprint('user',__name__,url_prefix='/user',template_folder='templates',static_folder='static')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@userRoute.before_request
def before_request():
    pass

@userRoute.route('/blog')
@login_required
def index():
    return  render_template("blog.html")

@userRoute.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if request.method =='GET':
        return render_template('login.html',form=form)
    if request.method =='POST':

        if not form.validate_on_submit():
            print(form.accountNumber.data)

            user = User.query.filter(User.accountNumber == form.accountNumber.data,
                                     User.password == form.password.data).first()
            if user:

                login_user(user)
                return render_template('blog.html')
    return render_template('login.html',form=form)



@userRoute.route('/sex',methods=['GET','POST'])
def sex():

    girl = Student.query.filter_by(bf_sex='男').count()
    boy = Student.query.filter_by(bf_sex='女').count()
    value=[girl,boy]
    name=['女','男']
    jsonData = {}
    jsonData['name'] = name
    jsonData['value'] = value
    j = json.dumps(jsonData)

    return (j)

@userRoute.route('/nation',methods=['GET','POST'])
def nation():

    words = ['%汉%','%满%','%回%','%朝鲜%']

    han = Student.query.filter(Student.bf_nation.like('%汉%')).count()
    man = Student.query.filter(Student.bf_nation.like('%满%')).count()
    hui = Student.query.filter(Student.bf_nation.like('%回%')).count()
    chaoxian = Student.query.filter(Student.bf_nation.like('%朝鲜%')).count()
    nameq = ['汉族','满族','回族','朝鲜族']
    valueq = [han,man,hui,chaoxian]

    jsonDataw = {}
    jsonDataw['nameq'] = nameq
    jsonDataw['valueq'] = valueq
    q = json.dumps(jsonDataw)

    return (q)

@userRoute.route('/birth',methods=['GET','POST'])
def birth():



    zero = Student.query.filter(Student.bf_BornDate.like('%2000%')).count()
    one = Student.query.filter(Student.bf_BornDate.like('%2001%')).count()
    two = Student.query.filter(Student.bf_BornDate.like('%2002%')).count()

    namew = ['2000','2001','2002']
    valuew = [zero,one,two]

    jsonDataw = {}
    jsonDataw['namew'] = namew
    jsonDataw['valuew'] = valuew
    q = json.dumps(jsonDataw)

    return (q)


