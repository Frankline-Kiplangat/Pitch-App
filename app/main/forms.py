from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email
from ..models import User, Comment, Pitch

class UpdateProfile (FlaskForm):
    """
    Class to update user profile
    """
    bio = TextAreaField ('Write something about you...', validators = [Required()])
    submit = SubmitField ('Submit')

# Class to create a wtf form for creating a pitch  
class PitchForm(FlaskForm):
    pitch = TextAreaField('Pitch',validators = [Required()])
    submit = SubmitField ('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment.',validators = [Required()])
    submit = SubmitField('Submit')  
    
class CategoryForm(FlaskForm):
     name = StringField ('Category name', validators = [Required()])
     submit = SubmitField('Post')


    