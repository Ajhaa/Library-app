from datetime import date, timedelta
from application import db, app
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.loans.models import Loan


@app.route("/books/<book_id>/loan", methods=["POST"])
@login_required
def loans_new(book_id):
  today = date.today()
  loan_end = today + timedelta(days=12)
  loan = Loan(loan_end)
  loan.book_id = book_id
  loan.user_id = current_user.id

  db.session().add(loan)
  db.session().commit()

  return redirect(url_for('books_show', book_id=book_id))

