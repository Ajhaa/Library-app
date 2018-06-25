from application import app, db
from flask import redirect, request, render_template, url_for
from application.genres.forms import GenreForm
from application.genres.models import Genre


@app.route("/genres/new", methods=["POST", "GET"])
def genres_new():
    if request.method == "GET":
        return render_template("genres/new.html", form = GenreForm())

    form = GenreForm(request.form)

    if not form.validate():
        return render_template("genres/new.html", form = form)

    new_genre = Genre(form.name.data)

    db.session().add(new_genre)
    db.session().commit()

    return redirect(url_for("books_index"))
