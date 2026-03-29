from flask import Flask,render_template
from flask_bootstrap import Bootstrap5
from data import hornets_starting_five 
from PIL import Image
import random

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
   #sends dicitonary to index.html
   return  render_template('index.html', dictionary = hornets_starting_five)


@app.route('/random')
def random_route():
    img1 = Image.open("static/images/lab16_image.jpg").convert("RGB")
    img2 = Image.open("static/images/lab16_image2.gif").convert("RGB")
    img3 = Image.open("static/images/lab16_image3.jpg").convert("RGB")

    images = [img1, img2, img3]
    
    #Chooses random image to applt negative alteration
    random_image = random.choice(images)

    negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in random_image.getdata()]
    random_image.putdata(negative_list)   

    # saves the altered image and sends it to random.html
    random_image.save("static/images/output.jpg")
    return render_template("random.html", image_file="images/output.jpg") 

# Boostrap Starter Template
@app.route('/bootstrap')
def bootstrap_page():
    return render_template('bootstrap.html')

