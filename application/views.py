from flask import render_template
from application import app

items = ["a", "b", "c"]

@app.route("/")
def index():
    return render_template("index.html", items=items)
