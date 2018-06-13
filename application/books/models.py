from application import db

from sqlalchemy.sql import text

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
                          nullable=False)

    author = db.relationship("Author", lazy=True)
    reviews = db.relationship("Review", cascade="delete", lazy=True)


    def __init__(self, title):
        self.title = title
        self.available = False

    @staticmethod
    def average_score(book_id):
        stmt = text("SELECT avg(score) FROM review"
                    " WHERE book_id = :id").params(id=book_id)
        res = db.engine.execute(stmt)

        return res.fetchone()[0]
