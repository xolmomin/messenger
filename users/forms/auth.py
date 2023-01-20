from django.forms import Form, EmailField, CharField


class SignUpGetVerificationForm(Form):
    pass


class SignUpForm(Form):
    email = EmailField()
