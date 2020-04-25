from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length


class AddFoodForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    exp_date = StringField('Exp Date', validators=[DataRequired()])
    picture = FileField("Add picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Add Food')