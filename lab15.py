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
