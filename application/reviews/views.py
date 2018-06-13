from flask import request, render_template, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm


@app.route("/reviews/<book_id>", methods=["GET", "POST"])
@login_required
def reviews_new(book_id):
    if request.method == "GET":
        return render_template("reviews/new.html", form=ReviewForm(), book_id=book_id)

    user_id = current_user.id
    form = ReviewForm(request.form)

    new_review = Review(form.score.data, form.text.data)
    new_review.user_id = user_id
    new_review.book_id = book_id

    db.session().add(new_review)
    db.session().commit()
    return redirect(url_for("books_show", book_id = book_id))

