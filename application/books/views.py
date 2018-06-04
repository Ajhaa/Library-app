from flask import render_template, request, redirect, url_for

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new")
def books_form():
    return render_template("books/new.html", form = BookForm())

@app.route("/books/", methods=["POST"])
def books_create():
    form = BookForm(request.form)
    if not form.validate():
        return render_template("books/new.html", form = form)
    title = form.title.data
    author = form.author.data
    new_book = Book(title, author)

    db.session().add(new_book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["POST"])
def change_availability(book_id):
    book = Book.query.get(book_id)
    book.available = not book.available
    db.session().commit()
    print("Hello there")
    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/delete/", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session().delete(book)
    db.session().commit()
    return redirect(url_for("books_index"))


