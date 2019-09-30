# Notes

- to start server run, `flask run` in root dir

#### check python 3 is installed
- run, `python3`
- to exit interactive interpreter run, `exit()`


#### Getting started

- set up virtual environment using `venv`, run `python3 -m venv venv`
- in root directory, activate it by running, `source venv/bin/activate`
- install flask in the activated environment, run `pip install flask`
- create app package dir
- create __init__ module
- create routes module 
- create main application module, platform
- in the terminal, run `export FLASK_APP=platform.py` to set the `FLASK_APP` environment variable and tell flask how to import platform.py
- to initialise the server and run the application, `flask run`
- click the URL to open the browser and you should see your message printed
- install python-dotenv, to register environment variables that i'd like to be automatically imported when i run the flask command `pip install python-dotenv` then `FLASK_APP=platform.py
`
- make templates dir and `index.html` with `{{ }}` placeholders blocks which represent the parts of the page that are a variable which will only be known at runtime
- in routes.py create mock object for user
- add `render_template('index.html', title='Home', user=user)`, `render_template()` is a function which invokes the Jinja2 template engine that comes with Flask
- add conditional statement for title in index.html using `{%  %}`, so if the view function forgets to pass a value for the title then the template will provide a default one
- add nav template in `base.html`
- to handle web form application in the Flask-WTF, run `pip install flask-wtf`

#### Project structure
```
platform/
   venv/
   app/
    __init__.py
    routes.py
    platform.py
```