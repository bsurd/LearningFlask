from flask import render_template, make_response, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bogdan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# @app.route('/get')
# def get_cookie():
#     myapp = request.cookies.get("myapp")
#     return "Cookie Content Is " + str(myapp)
#
#
# @app.route('/set')
# def set_cookie():
#     response = make_response("I have set the cookie")
#     response.set_cookie("my_app", "Flask Web Development")
