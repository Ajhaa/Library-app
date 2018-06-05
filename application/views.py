from flask import redirect, url_for
from application import app

items = ["a", "b", "c"]

@app.route("/")
def index():
    print("hello")
    return redirect(url_for('books_index'))
