from application import db

BookGenre = db.Table('bookgenre',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    books = db.relationship('Book', secondary=BookGenre, back_populates='genres', lazy=True)

    def __init__(self, name):
        self.name = name


