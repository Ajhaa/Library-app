from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, validators

class BookForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=1)])
    author = SelectField("Author", coerce=int)
    genre = SelectMultipleField("Genre", coerce=int)

    def update_choices(self, authors, genres):
        author_choices = []
        for author in authors:
            author_choices.append((author.id, author.name))
        self.author.choices = author_choices

        genre_choices = []
        for genre in genres:
            genre_choices.append((genre.id, genre.name))
        self.genre.choices = genre_choices



    class Meta:
        csrf = False
