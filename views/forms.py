from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, validators

from models import Newsletter

class EditNewsletter(FlaskForm):
    subject = StringField(
        label = 'Subject',
        validators = [validators.Length(min = 3, max = 100, message = 'Subject must be between 3-100 characters.'),
                      validators.DataRequired(message = 'Subject required')
                      ]
    )
    content = TextAreaField(
        label = 'Content'
    )
