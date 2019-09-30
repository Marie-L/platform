import os


# config settings are defined as a class
class Config(object):
    # specify the apps configuration options, use dictionary style The value of the secret key is set as an
    # expression with two terms - 1st term looks for the value of an environment variable, also called SECRET_KEY,
    # 2nd term is a hard coded string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask and some of its extensions use the value of the secret key as a cryptographic key, useful to generate
    # signatures or tokens. The Flask-WTF extension uses it to protect web forms against a nasty attack called
    # Cross-Site Request Forgery/ CSRF

