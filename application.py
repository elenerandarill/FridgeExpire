#!/usr/bin/python3
import datetime
import os
import secrets

from PIL import Image
from flask import Flask, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

from mainapp import app, db


@app.route('/')
@app.route('/home')
def home():
    from templates.models import Food
    foods = Food.query.order_by(Food.exp_date).all()
    today = datetime.date.today()
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
            flash("Food has been added.", "success")
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


@app.route('/food/<int:food_id>/delete', methods=['POST'])
def delete_food(food_id):
    from templates.models import Food
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    flash('Food has been deleted', 'info')
    return redirect(url_for('home'))



