# Importing form validation and rendering library integrated in Flask
from flask_wtf import FlaskForm
# Importing form file input field
from flask_wtf.file import FileField, FileAllowed
# Importing required field types
from wtforms import (StringField, SubmitField, TextAreaField)
# Importing field validators
from wtforms.validators import (DataRequired)


# Defining form for creating new post
#   including form validation parameters
class PostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    # For new post, uploading picture is required
    picture = FileField('Upload post picture',
                        validators=[DataRequired(),
                                    FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Post')


# Defining form for updating existing post
#   including form validation parameters
class UpdatePostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    # When updating post, if picture is not changed, originally uploaded
    #   picture is kept
    picture = FileField('Change post picture',
                        validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')
