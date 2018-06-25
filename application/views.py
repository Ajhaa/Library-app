from flask import render_template, url_for
from application import app
from application.books.models import Book

@app.route("/")
def index():
    return render_template("index.html", by_rating = Book.best_books(), by_loans = Book.top_loaned_books())
