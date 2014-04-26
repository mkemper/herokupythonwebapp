#-*- coding: utf-8 -*-

"""
Testapp for Flask and Heroku
2014/04/26
Marcus Kemper
"""

import os

from flask import Flask, render_template

# create the application
app = Flask(__name__)


# setting the route for root and 'hello'
@app.route('/')
@app.route('/hello')

# corresponding function
def hello():
    return render_template("index.html",title = 'TestApp',user = 'Gustave Gans')

@app.route('/hullo')
def hullo():
    return "Grsldmpf!"
