from flask import Flask, redirect, url_for, request
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)



from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in first"

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper




from application import views


from application.authors import models
from application.authors import views

from application.reviews import models
from application.reviews import views

from application.loans import models
from application.loans import views

from application.books import models
from application.books import views

from application.auth import models
from application.auth import views

from application.genres import models
from application.genres import views

from application.auth.models import User, Role



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def handle_needs_login():
    next=url_for(request.endpoint,**request.view_args)
    return redirect(url_for('auth_login', next=next))

from sqlalchemy import event

# initialize hardcoded values to tables after table creation
event.listen(Role.__table__, 'after_create', Role.init_roles)


db.create_all()

