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

# @app.route("/")
# def index():
#     return "Index page"

# @app.route("/hello")
# def hello():
#     return "<p>Hello World</p>"

@app.route("/route1")
def route1():
    return "<p>Testing routes: route 1</p>"

# @app.route("/sum")
# def sum(a, b):
#     return a + b 
#     print(sum(2, 7))

# a_argument = int(input('Type "a": '))
# b_argument = int(input('Type "b": '))

# print("Sum of a and b = ", sum (a_argument, b_argument))

# # OR just simulating fixed arguments direct:

# print ( "Sum of 2 and 3 = ", sum (2, 3) )



from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    # url_for('static', filename='style.css')


from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# from flask import request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()


# from flask import render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)



@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]

