"""
Lab 19: APIs
Name: Juan Zavala
Date: 04/13/2026
Class: CST 205 - Multimedia Programming
"""

from flask import Flask, render_template, request
import requests, json
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return render_template('search.html')

@app.route('/search')
def search():

    artist_name = request.args.get("artist_name")

    # The payload for the iTunes Search API request, including the search term and other parameters
    payload = {
        'term': artist_name,
        'entity': 'song',
        'limit': 5
    }

    # The iTunes Search API endpoint for searching songs by artist name
    url = "https://itunes.apple.com/search"


    try:
        r = requests.get(url, params=payload)
        data = r.json()
        results = data['results']
    except:
        results = []

    return render_template('result.html', results=results)