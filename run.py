from flask import Flask, render_template
app = Flask(__name__)

lista = ["yy", "kaa", "koo", "nee"]

@app.route("/")
def hello():
    return render_template("index.html", lista=lista)

if __name__ == "__main__":
    app.run(debug=True)
