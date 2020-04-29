from flask import Flask
app = Flask(__name__)


@app.route("/<int:num>")
def hello_world(num=0):
    return str(num)
