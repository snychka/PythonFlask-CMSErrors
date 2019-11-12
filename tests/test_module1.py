## Imports
import pytest
import re
import sqlite3

from pathlib import Path
from redbaron import RedBaron

from tests.utils import *
#!

## Paths
admin = Path.cwd() / 'cms' / 'admin'
admin_module = admin / '__init__.py'
models = admin / 'models.py'
auth = admin / 'auth.py'
#!

## Module Functions
def get_source_code(file_path):
    with open(file_path.resolve(), 'r') as source_code:
        return RedBaron(source_code.read())
#!

## Source Code
admin_module_code = get_source_code(admin_module)
models_code = get_source_code(models)
auth_code = get_source_code(auth)
#!

## Tests
@pytest.mark.test_disable_werkzeug_logging_module1
def test_disable_werkzeug_logging_module1():
    # 01.
    # from logging import getLogger
    # request_log = getLogger('werkzeug')
    # request_log.disabled = True
    assert False

@pytest.mark.test_configure_logging_module1
def test_models_configure_logging_module1():
    # 02.
    # def configure_logging(name, level):
    #     log = getLogger(name)
    #     log.setLevel(level)
    assert False

@pytest.mark.test_rotating_file_handler_module1
def test_models_rotating_file_handler_module1():
    # 03.
    # from logging.handlers import RotatingFileHandler
    # handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=5*1024*1024, backupCount=10)
    assert False

@pytest.mark.test_add_handler_module1
def test_models_add_handler_module1():
    # 04.
    # log.addHandler(handler)
    # return log
    assert False

@pytest.mark.test_timestamp_module1
def test_models_timestamp_module1():
    # 05.
    # from time import strftime
    # timestamp = strftime('[%d/%b/%Y %H:%M:%S]')
    assert False

@pytest.mark.test_access_log_module1
def test_modelsaccess_log__module1():
    # 06.
    # from logging import INFO, WARN, ERROR
    # access_log = configure_logging('access', INFO)
    assert False

@pytest.mark.test_after_request_module1
def test_models_after_request_module1():
    # 07.
    # @app.after_request
    # def after_request(response):
    #     return response
    assert False

@pytest.mark.test_access_log_format_module1
def test_models_access_log_format_module1():
    # 08.
    # access_log.info('%s - - %s "%s %s %s" %s -', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), response.status_code)
    assert False

@pytest.mark.test_valid_status_codes_module1
def test_models_valid_status_codes_module1():
    # 09.
    # if int(response.status_code) < 400:
    assert False
#!
