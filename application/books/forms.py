from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class BookForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=1)])
    author = SelectField("Author", coerce=int)

    def update_choices(self, authors):
        choices = []
        for author in authors:
            choices.append((author.id, author.name))
        self.author.choices = choices


    class Meta:
        csrf = False
