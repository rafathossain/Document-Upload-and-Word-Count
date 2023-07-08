import os

from dotenv import load_dotenv
from flask import Flask, request, session, url_for, redirect
from flask import render_template
from jinja2 import TemplateNotFound
from rq import Queue

from db import mydb
from tasks import count_words
from worker import conn

# Loading variable from env file
load_dotenv()

# Getting the queue from redis connection
q = Queue(connection=conn)

# Creating app and setting variables
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    """
    :param path: path of the template
    :return: Render template path with context variable
    """
    try:
        # Handling if there is any session message
        messages = session.get('messages')
        session['messages'] = []

        # Reconnecting to mysql db for updated data
        mydb.reconnect()

        # Creating a connection cursor
        cursor = mydb.cursor()

        # Fetch the last 5 records
        cursor.execute('''SELECT file_name, k, word_count, status FROM count_log ORDER BY id DESC LIMIT 5''')

        # Fetching the results
        results = cursor.fetchall()

        # Closing the cursor
        cursor.close()

        # Rendering the template with the data
        return render_template(path, messages=messages, results=results)
    except TemplateNotFound:
        # Rendering 404 page if template not found
        return render_template('page-404.html'), 404


@app.route('/upload', methods=['POST'])
def upload_document():
    """
    Handle the post request for file upload

    :return: Queue the file for processing and returns status message
    """
    # Checking if the file is available in request
    if 'file' not in request.files:
        session['messages'] = [{
            'tags': 'error',
            'text': 'No file uploaded.'
        }]
        return redirect(url_for('index'))

    file = request.files['file']

    # Checking if the file is not blank
    if file.filename == '':
        session['messages'] = [{
            'tags': 'error',
            'text': 'No file selected.'
        }]
        return redirect(url_for('index'))

    # Generating absolute file path
    filepath = os.path.join(app.root_path, 'media', file.filename)

    # Saving the file to system
    file.save(filepath)

    # Creating a connection cursor
    cursor = mydb.cursor()

    # Inserting the record
    cursor.execute(''' INSERT INTO count_log(`file_name`, `file_path`, `k`, `word_count`, `status`) VALUES(%s,%s,%s,%s,%s)''', (file.filename, filepath, request.form.get('word_length'), 0, "Processing"))
    row_id = cursor.lastrowid

    # Saving the Actions performed on the DB
    mydb.commit()

    # Closing the cursor
    cursor.close()

    # Queueing for background processing
    q.enqueue_call(func=count_words, args=(filepath, request.form.get('word_length'), row_id))

    # Set the successful session message
    session['messages'] = [{
        'tags': 'success',
        'text': 'File uploaded successfully and queued for counting.'
    }]
    return redirect(url_for('index'))
