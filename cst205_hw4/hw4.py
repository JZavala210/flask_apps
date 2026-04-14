"""
Name: Juan Zavala
Class: CST-205
Date: 04/07/2026
CST 205 — Multimedia Programming
Homework 4
"""
from flask import Flask,render_template
from flask_bootstrap import Bootstrap5
from PIL import Image
from image_info import image_info
import random
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    #Shuffle the image_info list and select the first 3 images to display on the index page
   random.shuffle(image_info)
   selected_images = image_info[:3]

   return render_template('index.html', images=selected_images)

@app.route('/detail/<image_id>')
def detail(image_id):
    image = None
    for img in image_info:
        if img['id'] == image_id:
            image = img

    """
    I tried putting the image path directly into the Image.open() function, but it didn't work. 
    So I had to use os.path.join() to get the correct path to the image.
    """
    image_path = os.path.join(app.root_path, 'static', 'images', image_id + '.jpg')

    # Open the image and get its mode, format, width, and height
    with Image.open(image_path) as img:
        mode = img.mode
        image_format = img.format
        width, height = img.size


    return render_template('detail.html', image=image, mode = mode, image_format = image_format, width = width, height = height)
 