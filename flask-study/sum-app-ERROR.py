from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def hello():
    return "<p>Hello World</p>"

@app.route("/route1")
def route1():
    return "<p>Testing routes: route 1</p>"

@app.route("/sum/<int:a>/<int:b>")
def sum (a=2, b=3):
    # a = request.args.get('a')
    # b = request.args.get('b')
    return str (a + b)
    return "<p> str (a + b) </p>"


# a_argument = int(input('Type "a": '))
# b_argument = int(input('Type "b": '))

# print("Sum of a and b = ", sum (a_argument, b_argument))

# # OR just simulating fixed arguments direct:

# print ( "Sum of 2 and 3 = ", sum (2, 3) )

# Enter the arguments 'a' and 'b' in browser address bar:
# http://127.0.0.1:5000/sum?a=2&b=3

