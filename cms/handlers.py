## Imports
from flask import request, render_template

from cms import app
from cms.admin.models import Content, Type
#!

from logging import getLogger # TASK(M01T01)
from logging.handlers import RotatingFileHandler # TASK(M01T03)
from time import strftime # TASK(M01T05)
from logging import INFO, WARN, ERROR # TASK(M01T06)
from traceback import format_exc # TASK(M02T05)

from cms.admin.auth import unauthorized # TASK(M03T04)

# TASK(M01T01)
request_log = getLogger('werkzeug')
request_log.disabled = True

# TASK(M01T02)
def configure_logging(name, level):
    log = getLogger(name)
    log.setLevel(level)
    # TASK(M01T03)
    handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=1024*1024, backupCount=10)
    # TASK(M01T04)
    log.addHandler(handler)
    return log

# TASK(M01T05)
timestamp = strftime('[%d/%b/%Y %H:%M:%S]')

# TASK(M01T06)
access_log = configure_logging('access', INFO)

@app.after_request # TASK(M01T07)
def after_request(response): # TASK(M01T07)
    if int(response.status_code) < 400: # TASK(M01T09)
        # TASK(M01T08)
        access_log.info('%s - - %s "%s %s %s" %s -', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), response.status_code)
    return response # TASK(M01T07)

# TASK(M02T01)
@app.context_processor
def inject_titles():
    titles = Content.query.with_entities(Content.slug, Content.title).join(Type).filter(Type.name == 'page')
    return dict(titles=titles)

# TASK(M02T02) Create `templates/not_found.html`

# TASK(M02T03)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

# TASK(M02T04)
error_log = configure_logging('error', ERROR)

@app.errorhandler(Exception) # TASK(M02T05)
def handle_exception(e): # TASK(M02T05)
    tb = format_exc() # TASK(M02T05)
    error_log.error('%s - - %s "%s %s %s" 500 -\n%s', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), tb) # TASK(M02T06)
    
    # TASK(M02T07) Create `templates/error.html`
    
    original = getattr(e, 'original_exception', None) # TASK(M02T08) 
    # TASK(M02T09)
    if original is None:
        return render_template('error.html'), 500
    #/
    return render_template('error.html', error=original), 500 # TASK(M02T08)

# TASK(M03T05)
unauthorized_log = configure_logging('unauthorized', WARN)
@unauthorized.connect # TASK(M03T07)
def log_unauthorized(app, user_id, username, **kwargs): # TASK(M03T06)
    unauthorized_log.warning('Unauthorized: %s %s %s', timestamp, user_id, username)
