#!/usr/bin/python3
import datetime
import os
import secrets

from PIL import Image
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = '2d65c65e323654552be29cc808a58eac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fooddata.db'
db = SQLAlchemy(app)



@app.route('/')
@app.route('/home')
def home():
    from templates.models import Food
    foods = Food.query.all()
    today = datetime.datetime.today()
    return render_template("home.html", foods=foods, today=today)


@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
    from forms import AddFoodForm
    from templates.models import Food
    form = AddFoodForm()
    if form.validate_on_submit():
        if form.picture.data:
            new_picname = save_picture(form.picture.data)
            food = Food(name=form.name.data, exp_date=form.exp_date.data, picture=new_picname)
            db.session.add(food)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add_food.html', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (128, 128)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


if __name__ == '__main__':
    app.run(debug=True)
