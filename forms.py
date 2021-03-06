from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, FileField, DateField, IntegerField
from wtforms.validators import DataRequired, Length


class BarCodeForm(FlaskForm):
    image_code = FileField('Upload image with barcode', validators=[FileAllowed(['jpg', 'png'])])
    input_code = StringField('Type barcode here', validators=[])
    submit = SubmitField('Add Barcode')


class NewBarForm(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    food_picture = FileField('Add Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add New Barcode')


class NewFoodForm(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    name = StringField('Name', validators=[])
    food_picture = FileField('Add Picture', validators=[FileAllowed(['jpg', 'png'])])
    food_picture_name = StringField('Food Picture Name')
    exp_date = DateField('Expiration date (yyyy-mm-dd)', validators=[DataRequired()])
    submit = SubmitField('Add New Food')


