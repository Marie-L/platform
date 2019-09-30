from flask import Flask
# from config module import Config class
from config import Config

# app variable is defined as an instance of class `Flask`, it's a member of the app package
app = Flask(__name__)

app.config.from_object(Config)

# routes is imported at the bottom as a workaround to circular imports,
from app import routes

