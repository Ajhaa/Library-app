from application import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.DateTime)

    books = db.relationship("Book", backref='account', lazy=True)

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return self.name
