from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField

class ReviewForm(FlaskForm):
    score = SelectField("Score", choices=[(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)])
    text = TextAreaField("Review text (optional)")

    class Meta:
        csrf = False
