from application import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    user = db.relationship("User", lazy=True)
    book = db.relationship("Book", lazy=True)

    def __init__(self, score, text):
        self.score = score
        self.text = text
