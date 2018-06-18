from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.authors.forms import AuthorForm
from application.authors.models import Author

@app.route("/authors/new", methods = ["POST", "GET"])
@login_required(role="ADMIN")
def authors_new():
    if request.method == "GET":
        return render_template("authors/new.html", form = AuthorForm())

    form = AuthorForm(request.form)

    if not form.validate():
        return render_template("authors/new.html", form = form)

    name = form.name.data
    birthdate = form.birthdate.data
    new_author = Author(name, birthdate)

    db.session().add(new_author)
    db.session().commit()
    return redirect(url_for("authors_list"))

@app.route("/authors/<author_id>/delete", methods = ["POST", "GET"])
@login_required(role="ADMIN")
def authors_delete(author_id):
    author = Author.query.get(author_id)

    db.session().delete(author)
    db.session().commit()

    return redirect(url_for("authors_list"))

@app.route("/authors")
def authors_list():
    return render_template("authors/list.html", authors=Author.query.all())

@app.route("/authors/<author_id>")
def authors_show(author_id):
    score = Author.average_score(author_id)
    if score != None:
        score = "%.2f" % score
    return render_template("authors/author.html", author=Author.query.get(author_id), score = score)


