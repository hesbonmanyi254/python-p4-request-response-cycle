# app/app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    host = request.host
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    app.run(port=5555)
