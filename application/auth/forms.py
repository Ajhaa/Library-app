from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, SelectField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    
    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=6)])
    role = SelectField("Role", choices=[(2, "Admin"), (1, "User")], coerce=int)

    class Meta:
        csrf = False

