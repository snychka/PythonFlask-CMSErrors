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
@pytest.mark.test__module3
def test_models__module3():
    # 01.
    # from blinker import Namespace # TASK(M03T01)
    # _signals = Namespace() # TASK(M03T01)
    assert False

@pytest.mark.test__module3
def test_models__module3():
    # 02.
    # unauthorized = _signals.signal('unauthorized')
    assert False

@pytest.mark.test__module3
def test_models__module3():
    # 03.
    # unauthorized.send(current_app._get_current_object(), user_id=user.id, username=user.username)
    assert False

@pytest.mark.test__module3
def test_models__module3():
    # 04.
    # from cms.admin.auth import unauthorized
    assert False

@pytest.mark.test__module3
def test_models__module3():
    # 05.
    # unauthorized_log = configure_logging('unauthorized', WARN)
    assert False

@pytest.mark.test__module3
def test_models__module3():
    # 06.
    # def log_unauthorized(app, user_id, username, **kwargs): # TASK(M03T06)
    #     unauthorized_log.warning('Unauthorized: %s %s %s', timestamp, user_id, username)
    assert False

@pytest.mark.test__module3
def test_models__module3():
    # 07.
    # @unauthorized.connect
    assert False
#!
