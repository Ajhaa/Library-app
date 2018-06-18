from application import db
from datetime import time

class Loan(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  start_date = db.Column(db.Date, default=db.func.current_date(), nullable=False)
  end_date = db.Column(db.Date, nullable=False)

  book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

  def __init__(self, end_date):
    self.end_date = end_date

  def is_active(self):
    return time.today() <= self.end_date  

      