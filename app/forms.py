# import FlaskForm base class
from flask_wtf import FlaskForm
# import 4 fields
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


# Flask-WTF extension uses Python classes to represent web forms, a form class defines the field of the form as class variables.

class LoginForm(FlaskForm):
    # form object - for each  one an object is created as a class variable in the LoginForm class
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')