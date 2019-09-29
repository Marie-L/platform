from flask import Flask, render_template
from app import app


# app.route decorator creates an association between URL given as an argument/ parameter and the function
# two routes are associated with this function
@app.route('/')
@app.route('/index')
def index():
    # mock object is used because user system hasn't been created yet
    user = {'username': 'Marie-Louise'}
    return render_template('index.html', title='Home', user=user)
