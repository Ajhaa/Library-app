from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class AuthorForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    birthdate = DateField("Birthdate")

    class Meta:
        csrf = False
