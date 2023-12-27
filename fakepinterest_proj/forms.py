from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest_proj.models import User

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmation_button = SubmitField('Sign in')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        
        if not user:
            raise ValidationError("Email doesn't exist. Please, Sign up.")


class FormSignUp(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8,30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")] )
    confirmation_button = SubmitField('Sign up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        
        if user:
            raise ValidationError("Email already registered. Please, Sign in.")
        

class FormPost(FlaskForm):
    post_image = FileField('Post Image', validators=[DataRequired()])
    confirm_post_button = SubmitField('Post')
