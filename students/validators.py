import datetime

from django.core.exceptions import ValidationError

ADULT_AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')
