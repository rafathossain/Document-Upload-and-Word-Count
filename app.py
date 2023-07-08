from flask import Flask, request, session, url_for, redirect
from flask import render_template
from jinja2 import TemplateNotFound
from worker import celery_init_app
import multiprocessing as mp


def create_flask_app() -> Flask:
    mp.set_start_method("fork")
    app = Flask(__name__)
    app.secret_key = "ASDADQWW$@#$"
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app


main_app = create_flask_app()
celery_app = main_app.extensions["celery"]


@main_app.route('/', defaults={'path': 'index.html'})
@main_app.route('/<path>')
def index(path):
    try:
        messages = session.get('messages')
        session['messages'] = []
        return render_template(path, messages=messages)
    except TemplateNotFound:
        return render_template('page-404.html'), 404


@main_app.route('/upload', methods=['POST'])
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

    # celery_app.send_task('tasks.count_words', kwargs={
    #     'file_path': '',
    #     'word_length': 10
    # })

    return 'File uploaded successfully.'
