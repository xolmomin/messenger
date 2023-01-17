from django.core.validators import RegexValidator

pattern = r'^(\+?998)?([. \-])?(\d[0-9])([. \-])?(\d){3}([. \-])?(\d){2}([. \-])?(\d){2}$'

phone_regex = RegexValidator(
    regex=r'^[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)
