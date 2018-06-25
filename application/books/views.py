from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.books.models import Book
from application.authors.models import Author
from application.reviews.models import Review
from application.books.forms import BookForm
from application.genres.models import Genre, BookGenre

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new")
@login_required(role="ADMIN")
def books_form():
    form = BookForm()
    form.update_choices(Author.query.all(), Genre.query.all())
    return render_template("books/new.html", form = form)

@app.route("/books/", methods=["POST"])
@login_required(role="ADMIN")
def books_new():
    form = BookForm(request.form)
    form.update_choices(Author.query.all(), Genre.query.all())
    if not form.validate():
        print(form)
        return render_template("books/new.html", form = form)
    title = form.title.data
    new_book = Book(title)
    new_book.author_id = form.author.data

    for id in form.genre.data:
        genre = Genre.query.get(id)
        new_book.genres.append(genre)

    db.session().add(new_book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["POST"])
@login_required(role="ADMIN")
def change_availability(book_id):
    book = Book.query.get(book_id)
    book.available = not book.available
    db.session().commit()
    return redirect(url_for("books_show", book_id=book_id))

@app.route("/books/<book_id>", methods=["GET"])
def books_show(book_id):
    score = Book.average_score(book_id)
    if score != None:
        score = "%.2f" % score
    return render_template("books/book.html", book = Book.query.get(book_id), score = score)

@app.route("/books/<book_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def books_delete(book_id):
    book = Book.query.get(book_id)

    db.session().delete(book)
    db.session().commit()

    return redirect(url_for("books_index"))


