from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.books.models import Book
from application.author.models import Author
from application.books.forms import BookForm

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new")
@login_required
def books_form():
    form = BookForm()
    form.update_choices(Author.query.all())
    return render_template("books/new.html", form = form)

@app.route("/books/", methods=["POST"])
@login_required
def books_new():
    form = BookForm(request.form)
    form.update_choices(Author.query.all())
    if not form.validate():
        print(form)
        return render_template("books/new.html", form = form)
    title = form.title.data
    new_book = Book(title)
    new_book.author_id = form.author.data

    db.session().add(new_book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def change_availability(book_id):
    book = Book.query.get(book_id)
    book.available = not book.available
    db.session().commit()
    print("Hello there")
    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/delete/", methods=["POST"])
@login_required
def book_delete(book_id):
    book = Book.query.get(book_id)
    db.session().delete(book)
    db.session().commit()
    return redirect(url_for("books_index"))


