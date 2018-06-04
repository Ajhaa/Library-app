from flask_wtf import FlaskForm
from wtforms import StringField, validators

class BookForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=1)])
    author = StringField("Author", [validators.Length(min=1)])

    class Meta:
        csrf = False
