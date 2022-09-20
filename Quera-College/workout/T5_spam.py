# todo: ^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$
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


def spam(num, content):
    # regex = r'^(?:09|\+989|00989)?(\d{9})$'
    # regex='[\w]'
    regex = r'\w \b[A-Za-z._]+@[A-Za-z]+\.[A-Za-z]{3}\b'
    #
    if not num.isnumeric() and (not re.match(regex, content) and not re.findall('spam', content.lower())):
        print("Not Spam")
    elif not num.isnumeric() and (re.match(regex, content) or re.findall('spam', content.lower())):
        print("Invalid Content")
    elif num.isnumeric() and not re.match(regex, content) and not re.findall('spam', content.lower()):
        print("Invalid Sender")
    elif num.isnumeric() and (re.match(regex, content) and re.findall('spam', content.lower())):
        print("Fully Invalid")
    elif not num.isnumeric() and (re.match(regex, content) and re.findall('spam', content.lower())):
        print("Invalid Content")
n = input()
c = input()
spam(n, c)