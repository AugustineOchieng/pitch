from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    title = StringField("Pitch Title")
    category = SelectField(
        u"Pitch Category",
        choices=[
            ("interviews", "interviews"),
            ("auditions", "auditions"),
            ("impressions", "impressions"),
        ],
    )
    pitch = TextAreaField("Pitch")
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):

    comment = TextAreaField("Comment")
    submit = SubmitField("Post Comments")


class UpdateProfile(FlaskForm):
    bio = TextAreaField("More info.", validators=[Required()])
    submit = SubmitField("Submit")

