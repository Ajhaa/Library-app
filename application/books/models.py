from application import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = False

    def __str__(self):
        return "%s: %s, available: %s" % (self.author, self.title, self.available)
