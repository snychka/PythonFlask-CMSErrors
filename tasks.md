# Module 1 - Access Log

## 1.1 - Disable Werkzeug Logging
[tag]: # "@pytest.mark.test_disable_werkzeug_logging_module1"
[code]: # "from logging import getLogger; request_log = getLogger('werkzeug'); request_log.disabled = True"


## 1.2 - Configure Logging
[tag]: # "@pytest.mark.test_configure_logging_module1"
[code]: # "def configure_logging(name, level): log = getLogger(name); log.setLevel(level)"


## 1.3 - Rotate File Handler
[tag]: # "@pytest.mark.test_rotating_file_handler_module1"
[code]: # "from logging.handlers import RotatingFileHandler; handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=5*1024*1024, backupCount=10)"


## 1.4 - Add Log Handler
[tag]: # "@pytest.mark.test_add_handler_module1"
[code]: # "log.addHandler(handler); return log"


## 1.5 - Timestamp Formatting
[tag]: # "@pytest.mark.test_timestamp_module1"
[code]: # "from time import strftime; timestamp = strftime('[%d/%b/%Y %H:%M:%S]')"


## 1.6 - Access Log
[tag]: # "@pytest.mark.test_access_log_module1"
[code]: # "from logging import INFO, WARN, ERROR; access_log = configure_logging('access', INFO)"


## 1.7 - After Request
[tag]: # "@pytest.mark.test_after_request_module1"
[code]: # "@app.after_request; def after_request(response): return response"


## 1.8 - Access Log Format
[tag]: # "@pytest.mark.test_access_log_format_module1"
[code]: # "    access_log.info('%s - - %s &quot;%s %s %s&quot; %s -', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), response.status_code)"


## 1.9 - Valid Status Codes
[tag]: # "@pytest.mark.test_valid_status_codes_module1"
[code]: # "if int(response.status_code) < 400:"


# Module 2 - Error Log

## 2.1 - Inject Titles
[tag]: # "@pytest.mark.test_inject_titles_module2"
[code]: # "@app.context_processor; def inject_titles(): titles = Content.query.with_entities(Content.slug, Content.title).join(Type).filter(Type.name == 'page'); return dict(titles=titles)"


## 2.2 - Not Found Template
[tag]: # "@pytest.mark.test_not_found_template_module2"
[code]: # "Create `templates/error.html`"


## 2.3 -Not Found Handler
[tag]: # "@pytest.mark.test_not_found_handler_module2"
[code]: # "@app.errorhandler(404); def page_not_found(e): return render_template('not_found.html'), 404"


## 2.4 - Error Log
[tag]: # "@pytest.mark.test_error_log_module2"
[code]: # "error_log = configure_logging('error', ERROR)"


## 2.5 - Error Handler
[tag]: # "@pytest.mark.test_error_handler_module2"
[code]: # "@app.errorhandler(Exception); def handle_exception(e): tb = format_exc()"


## 2.6 - Error Log Format
[tag]: # "@pytest.mark.test_error_log_format_module2"
[code]: # "error_log.error('%s - - %s &quot;%s %s %s&quot; 500 -\n%s', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), tb)"


## 2.7 - Error Template
[tag]: # "@pytest.mark.test_error_template_module2"
[code]: # "Create `templates/error.html`"


## 2.8 - Render Original Error Template
[tag]: # "@pytest.mark.test_render_original_error_template_module2"
[code]: # "original = getattr(e, 'original_exception', None)
return render_template('error.html', error=original), 500"


## 2.9 - Render Simple Error Template
[tag]: # "@pytest.mark.test_render_simple_error_template_module2"
[code]: # "if original is None: return render_template('error.html'), 500"


# Module 3 - Unauthorized Log

## 3.1 - Signals
[tag]: # "@pytest.mark.test_namespace_module3"
[code]: # "from blinker import Namespace; _signals = Namespace()"


## 3.2 - Unauthorized Signal
[tag]: # "@pytest.mark.test_unauthorized_signal_module3"
[code]: # "unauthorized = _signals.signal('unauthorized')"


## 3.3 - Send Unauthorized Signal
[tag]: # "@pytest.mark.test_send_unauthorized_signal_module3"
[code]: # "unauthorized.send(current_app._get_current_object(), user_id=user.id, username=user.username)"


## 3.4 - Import Unauthorized Signal
[tag]: # "@pytest.mark.test_import_unauthorized_signal_module3"
[code]: # "from cms.admin.auth import unauthorized"


## 3.5 - Unauthorized Log
[tag]: # "@pytest.mark.test_unauthorized_log_module3"
[code]: # "unauthorized_log = configure_logging('unauthorized', WARN)"


## 3.6 - Unauthorized Log Format
[tag]: # "@pytest.mark.test_unauthorized_log_format_module3"
[code]: # "def log_unauthorized(app, user_id, username, **kwargs): unauthorized_log.warning('Unauthorized: %s %s %s', timestamp, user_id, username)"


## 3.7 - Connect Decorator
[tag]: # "@pytest.mark.test_connect_decorator_module3"
[code]: # "@unauthorized.connect"

