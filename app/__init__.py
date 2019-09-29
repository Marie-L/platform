from flask import Flask

# app variable is defined as an instance of class `Flask`, it's a member of the app package
app = Flask(__name__)

# routes is imported at the bottom as a workaround to circular imports,
from app import routes

