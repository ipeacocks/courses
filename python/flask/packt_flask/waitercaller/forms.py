from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextField, validators
from wtforms.fields.html5 import EmailField


class RegistrationForm(FlaskForm):
    email = EmailField(
        'email',
        validators=[validators.DataRequired(), validators.Email()]
    )
    password = PasswordField(
        'password',
        validators=[validators.DataRequired(),
                    validators.Length(min=8,
                    message="Please choose a password of at least 8 characters")]
    )
    password2 = PasswordField(
        'password2',
        validators=[validators.DataRequired(),
                    validators.EqualTo('password', message="Passwords must match")]

    )
    submit = SubmitField('submit', [validators.DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField(
        'email',
        validators=[validators.DataRequired(), validators.Email()]
    )
    password = PasswordField(
        'password',
        validators=[validators.DataRequired(message="Password field is required")]
    )
    submit = SubmitField('submit', [validators.DataRequired()])


class CreateTableForm(FlaskForm):
    tablenumber = TextField(
        'tablenumber',
        validators=[validators.DataRequired()]
    )
    submit = SubmitField('createtablesubmit', [validators.DataRequired()])
