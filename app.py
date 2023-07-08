from flask import Flask, request, session, url_for, redirect
from flask import render_template
from jinja2 import TemplateNotFound
from rq import Queue
from rq.job import Job
from worker import conn
from tasks import count_words

q = Queue(connection=conn)

app = Flask(__name__)
app.secret_key = "ASDADQWW$@#$"


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        messages = session.get('messages')
        session['messages'] = []
        return render_template(path, messages=messages)
    except TemplateNotFound:
        return render_template('page-404.html'), 404


@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        session['messages'] = [{
            'tags': 'error',
            'text': 'No file uploaded.'
        }]
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        session['messages'] = [{
            'tags': 'error',
            'text': 'No file selected.'
        }]
        return redirect(url_for('index'))

    file.save('media/' + file.filename)

    job = q.enqueue_call(func=count_words, args=("file_path", "word_length"))
    print(job.get_id())

    return 'File uploaded successfully.'
