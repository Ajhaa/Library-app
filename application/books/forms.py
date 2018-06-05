from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class BookForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=1)])
    author = SelectField("Author", choices=[], coerce=int)

    class Meta:
        csrf = False
