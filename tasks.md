# Module 1 - Access Log

## 1.1 - Disable Werkzeug Logging
[tag]: # "@pytest.mark.test_disable_werkzeug_logging_module1"
[code]: # "from logging import getLogger; request_log = getLogger('werkzeug'); request_log.disabled = True"

### Module Overview
In this module we'll create a function to configure logging. The function creates and configures a rotating file handler. This function will then be used to configure an access log. Then using an `after_request` decorator we'll write all requests to this access log.

### First Task
By default, the Werzeug library logs each request to the console when debug mode is on. Let's disable this default log. Open the `cms/handlers.py` file, below the existing imports, import the `getLogger` method from `logging`.

Below the imports, call the `getLogger()` function and pass in the log we need, `'werkeug'`. Assign the result to a variable named `request_log`.
Then set the disabled property of `request_log` to `True`.

_Note: Unless otherwise noted, the rest of the tasks in this module happen in the file `cms/handlers.py`._

## 1.2 - Configure Logging
[tag]: # "@pytest.mark.test_configure_logging_module1"
[code]: # "def configure_logging(name, level): log = getLogger(name); log.setLevel(level)"

Below all other code, create a new function called `configure_logging`. The function should have two parameters, `name` and `level`. In the function body create a variable called log and assign it a call to the `getLogger()` function. Pass in `name`. 

On a new line call the `setLevel()` method on `log`. Pass in `level`.

## 1.3 - Rotate File Handler
[tag]: # "@pytest.mark.test_rotating_file_handler_module1"
[code]: # "from logging.handlers import RotatingFileHandler; handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=1024*1024, backupCount=10)"
Back at the top, by the other imports, import `RotatingFileHandler` from `logging.handlers`.

Return back to the `configure_logging` function and add a new variable called `handler`. Assign this variable a new `RotatingFileHandler`. Configure the instance with the file path `'logs/{}.log'.format(name)`. Also, set the max bytes to `1024*1024` and the backup count to `10`.

## 1.4 - Add Log Handler
[tag]: # "@pytest.mark.test_add_handler_module1"
[code]: # "log.addHandler(handler); return log"
Still in the `configure_logging` function add the `handler` to `log`. Finally, return the `log` from the function.

## 1.5 - Timestamp Formatting
[tag]: # "@pytest.mark.test_timestamp_module1"
[code]: # "from time import strftime; timestamp = strftime('[%d/%b/%Y %H:%M:%S]')"
Below the `configure_logging` function, use the `strftime()` method to get the current date and time. Format the date and time as follows: `[20/Nov/2019 14:59:12]`. Save the result in a variable named `timestamp`.

## 1.6 - Access Log
[tag]: # "@pytest.mark.test_access_log_module1"
[code]: # "from logging import INFO, WARN, ERROR; access_log = configure_logging('access', INFO)"
To log certain types of events import the levels `INFO`, `WARN`, and `ERROR` from the correct module.

With these imported, use the `configure_logging` function to create a log called `access.log`. **Hint: pass the correct `name`.** Make sure to log events at the `INFO` level. Save a reference to the result of this call in a variable called `access_log`.

## 1.7 - After Request
[tag]: # "@pytest.mark.test_after_request_module1"
[code]: # "@app.after_request; def after_request(response): return response"
Create a new function called `after_request`. It should have one parameter called `response`. In the body return `response`. Decorate the function with the `after_request` decorator. *Hint: Use `@app` as the first part of the decorator.* 

## 1.8 - Access Log Format
[tag]: # "@pytest.mark.test_access_log_format_module1"
[code]: # "access_log.info('%s - - %s "%s %s %s" %s -', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), response.status_code)"
We have at this point created an `access_log`. Let's now write all info level events to this log. Call the `info` method on `access_log` and pass in the following information in the order noted:

- Format: `'%s - - %s "%s %s %s" %s -'`
- Request remote address
- timestamp *Hint: Previously declared*
- Request method
- Request path
- Request scheme *Hint: Should be uppercase*
- Response status code

Example: `127.0.0.1 - - [20/Nov/2019 14:59:12] "GET / HTTP" 200 -`

## 1.9 - Valid Status Codes
[tag]: # "@pytest.mark.test_valid_status_codes_module1"
[code]: # "if int(response.status_code) < 400:"
The access log should only contain valid requests. Above the `info()` in the `after_request()` function add an `if` statement. The condition should check in the response status code is less than 400. *Hint: You will need to convert the status code to an `int()`.*

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
[code]: # "original = getattr(e, 'original_exception', None); return render_template('error.html', error=original), 500"


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
