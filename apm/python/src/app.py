from flask import Flask
import requests
import logging
import json_log_formatter


app = Flask("python-flask")
# Disable Flask's default logging
werkzeug = logging.getLogger('werkzeug')
werkzeug.disabled = True

# Set up a custom logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler()
json_handler.setFormatter(json_log_formatter.VerboseJSONFormatter())
json_handler.setLevel(logging.INFO)
log.addHandler(json_handler)
app.logger.propagate = False
log.propagate = False

@app.route('/')
def hello_world():
    return 'Flask: Hello World'

@app.route('/api')
def rest_hello_world():
    log.info("hello world - appoena")
    return '{"id":1,"message":"Flask: Hello World"}'


@app.route('/api/dotnet')
def rest_external():
    log.info('Calling external API')
    return requests.get('http://dotnet-todoapi:8081/api/todoitems').text

if __name__ == '__main__':
    app.run(host='0.0.0.0')