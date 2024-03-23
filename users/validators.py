from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator, _

class PhoneNumberValidator(RegexValidator):
    regex=r'^0[7-9][0-1]\d{8}$',
    message = _( 
          "your phone number should a valid number having the correct nigeria network code provider ",
    )

class NameValidator(UnicodeUsernameValidator):
	regex = r"^[\w]{3,150}\Z"
	message = _(
		"The name must be between 3 and 150 character and may contain letters."
	)