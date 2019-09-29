from flask import Flask, render_template
from app import app


# app.route decorator creates an association between URL given as an argument/ parameter and the function
# two routes are associated with this function
@app.route('/')
@app.route('/index')
def index():
    # mock object is used because user system hasn't been created yet
    user = {'username': 'Marie-Louise'}
    group = {'groupname': 'Truell Challenge'}
    # post mock object to represent posts using a list, each element is a dictionary
    posts = [
        {
            'author': {'username': 'John'},
            'group': {'groupname': 'Comms Team 1'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'group': {'groupname': 'Comms Team 2'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, group=group, posts=posts)
