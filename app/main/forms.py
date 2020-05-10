from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators = [Required()])
    comment = TextAreaField('Comment review')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Post title', validators = [Required()])
    post = TextAreaField('Blog Post', validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us a bit about yourself.', validators = [Required()])
    submit = SubmitField('Submit')