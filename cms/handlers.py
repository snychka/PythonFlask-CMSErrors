from cms import app

from flask import request, render_template
from cms.admin.models import Content, Type
from cms.admin import auth

import logging
import traceback
from time import strftime
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

@app.context_processor
def inject_titles():
    titles = Content.query.with_entities(Content.slug, Content.title).join(Type).filter(Type.name == 'page')
    return dict(titles=titles)

request_log = logging.getLogger('werkzeug')
request_log.disabled = True

default_handler.setFormatter(logging.Formatter('%(message)s'))

@app.after_request
def after_request(response):
    timestamp = strftime('[%d/%b/%Y %H:%M:%S]')
    if response.status_code < 400:
        app.logger.info('%s - - %s "%s %s %s" %s -', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), response.status_code)
    return response

access_handler = RotatingFileHandler('logs/access.log', maxBytes=10240, backupCount=10)
access_handler.setLevel(logging.INFO)
app.logger.addHandler(access_handler)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%d/%b/%Y %H:%M:%S]')
    app.logger.error('%s - - %s "%s %s %s" %s -\n%s', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), tb)
    original = getattr(e, 'original_exception', None)
    if original is None:
        return render_template('error.html'), 500
    return render_template('error.html', error=original), 500

error_handler = RotatingFileHandler('logs/error.log', maxBytes=10240, backupCount=10)
error_handler.setLevel(logging.ERROR)
app.logger.addHandler(error_handler)

unauthorized_handler = RotatingFileHandler('logs/unauthorized.log', maxBytes=10240, backupCount=10)
unauthorized_handler.setLevel(logging.WARN)
app.logger.addHandler(unauthorized_handler)

@auth.unauthorized.connect
def log_unauthorized(app, user_id, username, **kwargs):
    timestamp = strftime('%d/%b/%Y %H:%M:%S')
    app.logger.warning('Unauthorized: %s %s %s', timestamp, user_id, username)