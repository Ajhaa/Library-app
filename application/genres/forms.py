from flask_wtf import FlaskForm
from wtforms import StringField, validators

class GenreForm(FlaskForm):
    name = StringField("name", [validators.Length(min=1)])

    class Meta:
        csrf = False
