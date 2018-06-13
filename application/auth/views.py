from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    print("NEXT: %s" % request.args.get('next'))

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    print("NEXT: %s" % request.args.get('next'))

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Wrong username or password")

    print("User " + user.name + " was authenticated")
    login_user(user)
    return redirect_dest(home=url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new", methods = ["GET", "POST"])
def auth_new():
    if request.method == "GET":
        return render_template("auth/registrationform.html", form = NewUserForm())

    form = NewUserForm(request.form)
    if not form.validate():
        return render_template("auth/registrationform.html", form = form)

    name = form.name.data
    username = form.username.data
    password = form.password.data

    new_user = User(name, username, password)

    db.session().add(new_user)
    db.session().commit()
    return redirect(url_for("index"))

def redirect_dest(home):
    dest_url = request.args.get('next')
    
    if not dest_url:
        dest_url = home
    return redirect(dest_url)
