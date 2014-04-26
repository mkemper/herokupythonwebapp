import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')

def hello():
    return render_template("index.html",title = 'TestApp',user = 'Gustave Gans')
