"""
Name: Juan Zavala
Class: CST-205
Date: 03/23/2026
Lab 15:  Flask, Part 1

Link to repository: https://github.com/JZavala210/flask_apps 
"""
from flask import Flask,render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
   return """
    <h1>Hello, World!</h1>
    <p>Paulo C. : FIFO</p>
    """

@app.route('/juan')
def favorite_acronym():
    return render_template('templates.html')
