from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
