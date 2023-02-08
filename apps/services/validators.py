import datetime

from django.core.exceptions import ValidationError
from django.utils import timezone


def birth_date_validator(birth_date: datetime.date):
    minimal_date = datetime.date(day=1, month=1, year=1910)
    maximal_date = datetime.date(day=1, month=1, year=timezone.now().year - 11)

    if not minimal_date < birth_date < maximal_date:
        raise ValidationError("This date is invalid")
