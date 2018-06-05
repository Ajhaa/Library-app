from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class AuthorForm(FlaskForm):
    name = StringField("Name")
    birthdate = DateField("Birthdate")

    class Meta:
        csrf = False
