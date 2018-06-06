from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.author.forms import AuthorForm
from application.author.models import Author

@app.route("/author/new", methods = ["POST", "GET"])
@login_required
def author_new():
    if request.method == "GET":
        return render_template("author/createform.html", form = AuthorForm())
    form = AuthorForm(request.form)
    if not form.validate():
        return render_template("author/createform.html", form = form)
    name = form.name.data
    birthdate = form.birthdate.data
    new_author = Author(name, birthdate)

    db.session().add(new_author)
    db.session().commit()
    return redirect(url_for("author_list"))

@app.route("/author")
def author_list():
    return render_template("author/list.html", authors=Author.query.all())

@app.route("/author/<author_id>")
def author_show(author_id):
    return render_template("author/author.html", author=Author.query.get(author_id))
