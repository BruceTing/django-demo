from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_email(value):
    if not value.endswith('.com'):
        raise ValidationError(
            _('%(value)s is not a valid email'),
            params={'value': value}
        )

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value}
        )

