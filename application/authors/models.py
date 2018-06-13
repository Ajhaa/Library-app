from application import db

from sqlalchemy.sql import text

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.DateTime)

    books = db.relationship("Book", cascade="delete", lazy=True)

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return self.name

    @staticmethod
    def average_score(author_id):
        stmt = text("SELECT avg(score) FROM review"
                    " LEFT JOIN book ON review.book_id = book.id"
                    " LEFT JOIN author ON book.author_id = :id").params(id=author_id)
        res = db.engine.execute(stmt)

        return res.fetchone()[0]
