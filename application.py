#!/usr/bin/python3
import datetime
import os
import secrets

from PIL import Image
from flask import Flask, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from pyzbar.pyzbar import decode
from mainapp import app, db


@app.route('/')
@app.route('/home')
def home():
    from models import NewFood
    foods = NewFood.query.order_by(NewFood.exp_date).all()
    today = datetime.date.today()
    return render_template("home.html", foods=foods, today=today)


@app.route('/barcode/find', methods=['GET', 'POST'])
def find_barcode():
    from models import BarFood
    from forms import BarCodeForm
    form = BarCodeForm()
    if form.validate_on_submit():
        b_code = (get_barcode(form)).decode("utf-8")
        if b_code != 'empty':
            the_bar = BarFood.query.filter_by(barcode=b_code).first()
            if the_bar:
                # KNOWN barcode
                return redirect(url_for("disp_add_new_food_form", barcode=b_code))
            else:
                # NEW barcode
                return redirect(url_for("disp_add_barform", barfood_barcode=b_code))
        else:
            flash("Try adding barcode again.", "info")
            return redirect(url_for("find_barcode"))
    return render_template("find_barcode.html", form=form)


def get_barcode(form):
    if form.input_code.data:
        b_code = form.input_code.data
        return b_code
    elif form.image_code.data:
        picture = form.image_code.data
        i = Image.open(picture)
        i.save("static/images/barcode.jpg")
        bar_info = decode(Image.open("static/images/barcode.jpg"))
        for barcode in bar_info:
            b_code = barcode.data
            return b_code
    else:
        return 'empty'


# wyswietla formularz z barcodem
@app.route('/display_add_barcode_form/<string:barfood_barcode>')
def disp_add_barform(barfood_barcode):
    from forms import NewBarForm
    form = NewBarForm()
    form.barcode.data = barfood_barcode
    return render_template("add_new_bar.html", form=form)


# otrzymuje kolejne dane z formularza
@app.route('/add_barcode', methods=['POST'])
def insert_new_bar():
    from forms import NewBarForm
    from models import BarFood
    form = NewBarForm()
    if form.validate_on_submit():
        food_pic = save_foodimage(form.food_picture.data)
        barfood = BarFood(barcode=form.barcode.data, name=form.name.data, image_code=food_pic)
        db.session.add(barfood)
        db.session.commit()
        flash("It has been added!", "success")
        return redirect(url_for("disp_add_new_food_form", barcode=barfood.barcode))
    flash("Something went wrong with the form.", "danger")
    return render_template("add_new_bar.html", form=form)


def save_foodimage(form_img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_img.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (128, 128)
    i = Image.open(form_img)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route('/food/<string:barcode>/add', methods=['GET', 'POST'])
def disp_add_new_food_form(barcode):
    from forms import NewFoodForm
    from models import BarFood, NewFood
    form = NewFoodForm()
    form.barcode.data = barcode
    barfood = BarFood.query.filter_by(barcode=barcode).first()
    form.name.data = barfood.name
    form.food_picture_name.data = barfood.image_code
    if form.validate_on_submit():
        new_food = NewFood(barcode=barfood.barcode, name=barfood.name, food_picture=barfood.image_code, exp_date=form.exp_date.data)
        db.session.add(new_food)
        db.session.commit()
        flash("New food has been added.", "success")
        return redirect(url_for("home"))
    return render_template("add_new_food.html", form=form, barcode=barcode)


@app.route('/food/<int:food_id>/delete', methods=['POST'])
def delete_food(food_id):
    from models import NewFood
    food = NewFood.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    flash('Food has been deleted', 'info')
    return redirect(url_for('home'))



