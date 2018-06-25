from application import db
from application.genres.models import BookGenre
from sqlalchemy.sql import text

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
                          nullable=False)

    author = db.relationship("Author", lazy=True)
    reviews = db.relationship("Review", cascade="delete", lazy=True)

    genres = db.relationship("Genre", secondary=BookGenre, back_populates='books',lazy=True)


    def __init__(self, title):
        self.title = title
        self.available = False

    @staticmethod
    def average_score(book_id):
        stmt = text("SELECT avg(score) FROM review"
                    " WHERE book_id = :id").params(id=book_id)
        res = db.engine.execute(stmt)

        return res.fetchone()[0]

    @staticmethod
    def best_books():
        stmt = text("SELECT book.id, book.title, AVG(review.score) as avg FROM book, review"
                    " WHERE review.book_id = book.id"
                    " GROUP BY book.id"
                    " ORDER BY avg DESC"
                    " LIMIT 5")
        res = db.engine.execute(stmt)

        books = []
        for row in res:
            books.append((row[0], row[1], row[2]))

        return books

    @staticmethod
    def top_loaned_books():
        stmt = text("SELECT book.id, book.title, COUNT(loan.id) as loans FROM book, loan"
                    " WHERE loan.book_id = book.id"
                    " GROUP BY book.id"
                    " ORDER BY loans desc"
                    " LIMIT 5")
        res = db.engine.execute(stmt)

        books = []
        for row in res:
            books.append((row[0], row[1], row[2]))

        return books
