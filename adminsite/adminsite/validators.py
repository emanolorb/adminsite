from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re


def validate_phone_number(value):
    try:
        patron = re.compile('\A(\+?521?|044|045|01)?[0-9]{10}\Z')
        if patron.search(value) is None:
            raise ValidationError(
                _('%(value)s is not a phone number'),
                params={'value': value},
            )
    except:
        raise ValidationError(
            _('%(value)s is not a phone number'),
            params={'value': value},
        )
