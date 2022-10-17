import re


def spam(num, content):
    regex = '[^a-zA-Z\d\s:]'
    x = re.sub(regex, '', content)
    print(len(x))
    print(len(content))
    print(bool(re.findall('spam', content.lower())))
    if not num.isnumeric() and not ((len(x) < (len(content) / 2)) and re.findall('spam', content.lower())):
        print("Not Spam")
    elif not num.isnumeric() and (len(x) < (len(content) / 2)) and re.findall('spam', content.lower()):
        print("Invalid Content")
    elif num.isnumeric() and not ((len(x) < (len(content) / 2)) and re.findall('spam', content.lower())):
        print("Invalid Sender")
    elif num.isnumeric() and (re.match(regex, content) or re.findall('spam', content.lower())):
        print("Fully Invalid")


# -------------------------------------------------------------

# n = input()
# c = input()
# spam(n, c)
#
#
# def countInvalidChar(content):
#     count = 0
#     for c in content:
#         if not c.isalnum() and c != ' ':
#             count += 1
#     return count
#
#
# user = input()
# content = input()
#
# isInvalidSender = user.isdigit()
# isInvalidContent = countInvalidChar(content) > (len(content) / 2) and 'spam' in content.lower()
#
# if isInvalidContent and isInvalidSender:
#     print('Fully Invalid')
#
# elif isInvalidContent:
#     print('Invalid Content')
#
# elif isInvalidSender:
#     print('Invalid Sender')
#
# else:
#     print('Not Spam')
#