from django.forms import Form, EmailField, CharField


class SignUpGetVerificationForm(Form):
    email = EmailField()


class SignUpVerifyForm(SignUpGetVerificationForm):
    code = CharField(max_length='8')
