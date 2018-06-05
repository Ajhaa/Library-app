from application import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
                          nullable=False)

    author = db.relationship("Author", lazy=True)

    def __init__(self, title):
        self.title = title
        self.available = False

