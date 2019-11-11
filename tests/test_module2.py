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
@pytest.mark.test__module2
def test_models__module2():
    # 01.
    # @app.context_processor
    # def inject_titles():
    #     titles = Content.query.with_entities(Content.slug, Content.title).join(Type).filter(Type.name == 'page')
    #     return dict(titles=titles)
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 02.
    # Create `templates/not_found.html`
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 03.
    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return render_template('not_found.html'), 404
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 04.
    # error_log = configure_logging('error', ERROR)
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 05.
    # @app.errorhandler(Exception)
    # def handle_exception(e):
    #     tb = format_exc()
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 06.
    # error_log.error('%s - - %s "%s %s %s" 500 -\n%s', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), tb)
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 07.
    # Create `templates/error.html`
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 08.
    # original = getattr(e, 'original_exception', None) # TASK(M02T08) 
    # return render_template('error.html', error=original), 500 # TASK(M02T08)
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 09.
    # if original is None:
    #     return render_template('error.html'), 500
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 10.
    # Create `admin/templates/admin/not_found.html`
    assert False

@pytest.mark.test__module2
def test_models__module2():
    # 11.
    # @admin_bp.app_errorhandler(404)
    # def page_not_found(e):
    #     return render_template('admin/not_found.html'), 404
    assert False
#!
