from app import app
from flask import render_template


@app.route('/')
def index():
    text = 'flask_blog_engine'
    return render_template('index.html', t=text)
