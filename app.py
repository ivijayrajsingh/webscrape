# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:13:27 2021

@author: vijay
"""

from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return "<h1>Heroku deployment</h1>"

if __name__ == "__main__":
    app.run(debug=True)