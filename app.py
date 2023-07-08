from flask import Flask
from flask import render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        return render_template(path)
    except TemplateNotFound:
        return render_template('page-404.html'), 404
