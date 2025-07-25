"""
This file contains class that are used to create SignUpForm for the application.
"""

from wtforms import (
    EmailField,
    Form,
    PasswordField,
    StringField,
    validators,
)


class SignUpForm(Form):
    """
    This class creates a form for signing up.
    """

    userName = StringField(
        "Username",
        [validators.Length(min=4, max=25), validators.InputRequired()],
    )

    email = EmailField(
        "Email",
        [validators.Length(min=6, max=50), validators.InputRequired()],
    )

    password = PasswordField(
        "Password",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
    )

    passwordConfirm = PasswordField(
        "passwordConfirm",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
    )
