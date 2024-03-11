# save this as app.py
# from flask import Flask, request
# from markupsafe import escape

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {escape(name)}!'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Original app.py / hello.py is above
