## Imports
import pytest
import re
import sqlite3

from pathlib import Path
from redbaron import RedBaron

from tests.utils import *
#!

## Paths
handlers = Path.cwd() / 'cms' / 'handlers.py'
auth = Path.cwd() / 'cms' / 'admin' / 'auth.py'
#!

## Module Functions
def get_source_code(file_path):
    with open(file_path.resolve(), 'r') as source_code:
        return RedBaron(source_code.read())
#!

## Source Code
handlers_code = get_source_code(handlers)
auth_code = get_source_code(auth)
#!de = get_source_code(auth)
#!


## Tests
@pytest.mark.test_inject_titles_module2
def test_models_inject_titles_module2():
    # 01. Inject Titles
    # @app.context_processor
    # def inject_titles():
    #     titles = Content.query.with_entities(Content.slug, Content.title).join(Type).filter(Type.name == 'page')
    #     return dict(titles=titles)
    inject_titles = handlers_code.find('def', name='inject_titles')
    inject_titles_exists = inject_titles is not None
    assert inject_titles_exists, \
        'Have you created a function called `inject_titles` with a parameter of `response`?'

    decorator_exists = inject_titles.find('decorator', lambda node: node.find('dotted_name', lambda node: \
          node.value[0].value == 'app' and \
          node.value[1].type == 'dot' and \
          node.value[2].value == 'context_processor')) is not None
    assert decorator_exists, \
        'The `inject_titles` function should have a decorator of `@app.context_processor`.'

    titles = inject_titles.find('assign', lambda node: node.target.value == 'titles')
    titles_exists = titles is not None
    assert titles_exists, \
        'Are you setting the `titles` variable correctly?'
    with_entities_call = titles.find('atomtrailers', lambda node: \
        node.value[0].value == 'Content' and \
        node.value[1].value == 'query' and \
        node.value[2].value == 'with_entities' and \
        node.value[3].type == 'call'
        )

    with_entities_call_node = with_entities_call.find('name', value='with_entities').next
    with_entities_args = get_args(with_entities_call_node)

    slug_arg = 'Content.slug' in with_entities_args
    assert slug_arg, \
        'Are you passing `Content.slug` to the `with_entities()` function?'

    title_arg = 'Content.slug' in with_entities_args
    assert title_arg, \
        'Are you passing `Content.title` to the `with_entities()` function?'

    join_call = with_entities_call.find('name', value='join').next
    join_args = get_args(join_call)

    type_arg = 'Type' in join_args
    assert type_arg, \
        'Are you passing `Type` to the `join()` function?'

    filter_call = with_entities_call.find('name', value='filter').next
    filter_args = get_args(filter_call)

    page_arg = 'Type.name=="page"' in filter_args
    assert page_arg, \
        'Are you passing the correct condition to the `filter()` function?'

    return_dict = inject_titles.find('return', lambda node: \
        node.value[0].value == 'dict' and \
        node.value[1].type == 'call')
    return_dict_exists = return_dict is not None
    assert return_dict_exists, \
        'Are you returning a `dict()`?'

    return_dict_args = 'titles:titles' in get_args(return_dict.find('call'))
    assert return_dict_args, \
        'Are you passing the `titles` with a `titles` keyword argument to `dict()`?'

'''
@pytest.mark.test_not_found_template_module2
def test_models_not_found_template_module2():
    # 02. Not Found Template
    # Create `templates/not_found.html`
    assert False
'''

@pytest.mark.test_not_found_handler_module2
def test_models_not_found_handler_module2():
    # 03. Not Found Handler
    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return render_template('not_found.html'), 404
    def_page_not_found = handlers_code.find('def', lambda node: \
        node.name == 'page_not_found' and \
        node.arguments[0].target.value == 'e')

    decorator = def_page_not_found.find('decorator', lambda node: node.find('dotted_name', lambda node: \
          node.value[0].value == 'app' and \
          node.value[1].type == 'dot' and \
          node.value[2].value == 'errorhandler' and \
          node.parent.call.value[0].value.value == '404'))

    decorator_exists = decorator is not None
    assert decorator_exists, \
        'The `page_not_found` function should have a decorator of `@app.errorhandler(404)`.'

    return_404 = def_page_not_found.find('tuple', lambda node: \
        node.parent.type == 'return' and \
        node.value[0].value[0].value == 'render_template' and \
        node.value[0].value[1].value[0].value.value.replace("'", '"') == '"not_found.html"' and \
        node.value[-1].value == '404') is not None
    assert return_404, \
        'The `page_not_found` function should render the `not_found.html` template with a `404`.'


@pytest.mark.test_error_log_module2
def test_error_log_module2():
    # 04. Error Log
    # error_log = configure_logging('error', ERROR)
    error_log = handlers_code.find('assign', lambda node: node.target.value == 'error_log')
    error_log_exists = error_log is not None
    assert error_log_exists, \
        'Are you setting the `error_log` variable correctly?'

    configure_logging_call = error_log.find('atomtrailers', lambda node: \
        node.value[0].value == 'configure_logging' and \
        node.value[1].type == 'call'
        )
    configure_logging_call_exists = configure_logging_call is not None
    assert configure_logging_call_exists, \
        'Are you calling the `configure_logging()` function and assigning the result to `error_log`?'

    configure_logging_args = get_args(configure_logging_call[1])

    arg_count = len(configure_logging_args) == 2
    assert arg_count, \
        'Are you passing the correct number of arguments to `configure_logging()`?'

    first_arg = configure_logging_args[0] == '"error"'
    assert first_arg, \
        'Are you passing the correct name to `configure_logging()`?'

    second_arg = configure_logging_args[1] == 'ERROR'
    assert second_arg, \
        'Are you passing the correct level to `configure_logging()`?'

@pytest.mark.test_error_handler_module2
def test_models_error_handler_module2():
    # 05. Error Handler
    # from traceback import format_exc
    # @app.errorhandler(Exception)
    # def handle_exception(e):
    #     tb = format_exc()
    traceback_import = get_imports(handlers_code, 'traceback')
    traceback_import_exits = traceback_import is not None
    assert traceback_import_exits, \
        'Do you have a `traceback` import statement?'
    format_exc_exists = 'format_exc' in traceback_import
    assert format_exc_exists, \
        'Are you importing `format_exc` from `traceback` in `cms/handlers.py`?'

    def_handle_exception = handlers_code.find('def', lambda node: \
        node.name == 'handle_exception' and \
        node.arguments[0].target.value == 'e')
    def_handle_exception_exists = def_handle_exception is not None
    assert def_handle_exception_exists, \
        'Have you created a function called `handle_exception` with a parameter of `e`?'

    decorator = def_handle_exception.find('decorator', lambda node: node.find('dotted_name', lambda node: \
          node.value[0].value == 'app' and \
          node.value[1].type == 'dot' and \
          node.value[2].value == 'errorhandler' and \
          node.parent.call.value[0].value.value == 'Exception'))

    decorator_exists = decorator is not None
    assert decorator_exists, \
        'The `page_not_found` function should have a decorator of `@app.errorhandler(Exception)`.'

    tb = def_handle_exception.find('assign', lambda node: node.target.value == 'tb')
    tb_exists = tb is not None
    assert tb_exists, \
        'Are you setting the `tb` variable correctly?'
    format_exc_call = tb.find('atomtrailers', lambda node: \
        node.value[0].value == 'format_exc' and \
        node.value[1].type == 'call'
        )
    format_exc_call_exists = format_exc_call is not None
    assert format_exc_call_exists, \
        'Are you calling the `format_exc_call()` function and assigning the result to `tb`?'

@pytest.mark.test_error_log_format_module2
def test_models_error_log_format_module2():
    # 06. Error Log Format
    # error_log.error('%s - - %s "%s %s %s" 500 -\n%s', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), tb)
    # info_call = after_request.find('atomtrailers', lambda node: \
    #     node.value[0].value == 'access_log' and \
    #     node.value[1].value == 'info' and \
    #     node.value[2].type == 'call')
    # info_call_exists = info_call is not None
    # assert info_call_exists, \
    #     'Are you calling the `access_log.info()` function?'

    # info_args = get_args(info_call[-1], False)

    # arg_count = len(info_args) == 7
    # assert arg_count, \
    #     'Are you passing the correct number of arguments to `access_log.info()`?'

    # first_arg = info_args[0] == '\'%s - - %s "%s %s %s" %s -\'' 
    # assert first_arg, \
    #     'Are you passing the correct log format to `access_log.info()` as the first argument?'

    # second_arg = info_args[1] == 'request.remote_addr' 
    # assert second_arg, \
    #     'Are you passing the `request.remote_addr` to `access_log.info()` as the second argument?'

    # third_arg = info_args[2] == 'timestamp' 
    # assert third_arg, \
    #     'Are you passing `timestamp` to `access_log.info()` as the third argument?'

    # fourth_arg = info_args[3] == 'request.method' 
    # assert fourth_arg, \
    #     'Are you passing `request.method` to `access_log.info()` as the fourth argument?'

    # fifth_arg = info_args[4] == 'request.path' 
    # assert fifth_arg, \
    #     'Are you passing `request.path` to `access_log.info()` as the fifth argument?'

    # sixth_arg = info_args[5] == 'request.scheme.upper()' 
    # assert sixth_arg, \
    #     'Are you passing `request.scheme.upper()` to `access_log.info()` as the sixth argument?'

    # seventh_arg = info_args[6] == 'response.status_code' 
    # assert seventh_arg, \
    #     'Are you passing `response.status_code` to `access_log.info()` as the seventh argument?'

    assert False

'''
@pytest.mark.test_error_template_module2
def test_models_error_template_module2():
    # 07. Error Template
    # Create `templates/error.html`
    assert False

@pytest.mark.test_render_original_error_template_module2
def test_models_render_original_error_template_module2():
    # 08. Render Original Error Template
    # original = getattr(e, 'original_exception', None)
    # return render_template('error.html', error=original), 500
    assert False

@pytest.mark.test_render_simple_error_template_module2
def test_models_render_simple_error_template_module2():
    # 09. Render Simple Error Template
    # if original is None:
    #     return render_template('error.html'), 500
    assert False
'''