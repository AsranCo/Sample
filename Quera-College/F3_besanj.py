##بسنج
#todo: ^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$
# └─────┬────┘└───┬──┘└─────┬─────┘└─────┬─────┘ └───┬───┘
# │         │         │            │           no _ or . at the end
# │         │         │            │
# │         │         │            allowed characters
# │         │         │
# │         │         no __ or _. or ._ or .. inside
# │         │
# │         no _ or . at the beginning
# │
# username is 8-20 characters long

import re


def validate_email(email):
    regex = r'\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{3}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


def validate_phone(number):
    regex = r'^(?:09|\+989|00989)?(\d{9})$'
    if (re.fullmatch(regex, number)):
        return True
    else:
        return False
