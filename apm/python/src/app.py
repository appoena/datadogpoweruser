from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask: Hello World'

@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World"}'


@app.route('/api/dotnet')
def rest_external():
    return requests.get('http://dotnet-todoapi:8081/api/todoitems').text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')