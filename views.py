#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Testapp for Flask and Heroku
2014/04/26
Marcus Kemper
"""

import os

from flask import Flask, render_template
import test
from forms import LoginForm

# create the application
app = Flask(__name__)

# use config.py
app.config.from_object('config')

# setting the route for root and 'hello'
@app.route('/')
@app.route('/hello')

# corresponding function
def hello():
    return render_template("index.html",title = 'TestApp',user = 'General Gustave Gans')

@app.route('/hullo')
def hullo():
    return "Grsldmpf!"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)

