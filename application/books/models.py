from application import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #isbn = db.Column(db.String(13), nullable=False)
    #pub_year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    #author = db.Column(db.String, nullable=False)

    def __init__(self, title):
        #self.isbn = isbn
        #self.pub_year = pub_year
        self.title = title
        #self.author = author
