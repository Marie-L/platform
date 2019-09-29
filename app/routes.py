from app import app

# app.route decorator creates an association between URL given as an argument/ parameter and the function
# two routes are associated with this function
@app.route('/')
@app.route('/index')
def index():
    return "hello, World!"