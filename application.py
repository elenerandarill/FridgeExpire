#!/usr/bin/python3
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SECRET-KEY'] = 'jedzonko'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fooddata.db'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    from templates.models import Food
    foods = Food.query.all()
    return render_template("home.html", foods=foods)


if __name__ == '__main__':
    app.run(debug=True)
