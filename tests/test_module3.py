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
login_template = template_data('login')
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
@pytest.mark.test_namespace_module3
def test_models_namespace_module3():
    # 01.
    # from blinker import Namespace
    # _signals = Namespace()
    assert False

@pytest.mark.test_unauthorized_signal_module3
def test_models_unauthorized_signal_module3():
    # 02.
    # unauthorized = _signals.signal('unauthorized')
    assert False

@pytest.mark.test_send_unauthorized_signal_module3
def test_models_send_unauthorized_signal_module3():
    # 03.
    # unauthorized.send(current_app._get_current_object(), user_id=user.id, username=user.username)
    assert False

@pytest.mark.test_import_unauthorized_signal_module3
def test_models_import_unauthorized_signal_module3():
    # 04.
    # from cms.admin.auth import unauthorized
    assert False

@pytest.mark.test_unauthorized_log_module3
def test_models_unauthorized_log_module3():
    # 05.
    # unauthorized_log = configure_logging('unauthorized', WARN)
    assert False

@pytest.mark.test_unauthorized_log_format_module3
def test_models_unauthorized_log_format_module3():
    # 06.
    # def log_unauthorized(app, user_id, username, **kwargs): # TASK(M03T06)
    #     unauthorized_log.warning('Unauthorized: %s %s %s', timestamp, user_id, username)
    assert False

@pytest.mark.test_connect_decorator_module3
def test_models_connect_decorator_module3():
    # 07.
    # @unauthorized.connect
    assert False
#!
