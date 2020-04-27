from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2d65c65e323654552be29cc808a58eac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fooddata.db'
db = SQLAlchemy(app)
