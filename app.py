from flask import Flask

app = Flask(__name__)

@app.get('/')
def test():
    return "Hello, World!"