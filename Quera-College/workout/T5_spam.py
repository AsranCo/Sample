import re


def spam(num, content):
    regex = '[^a-zA-Z\d\s:]'
    x = re.sub(regex, '', content)
    print(len(x))
    print(len(content))
    print(bool(re.findall('spam', content.lower())))
    if not num.isnumeric() and not ((len(x) < (len(content) / 2)) and  re.findall('spam', content.lower())):
        print("Not Spam")
    elif not num.isnumeric() and (len(x) < (len(content) / 2)) and re.findall('spam', content.lower()):
        print("Invalid Content")
    elif num.isnumeric() and not ((len(x) < (len(content) / 2)) and  re.findall('spam', content.lower())):
        print("Invalid Sender")
    elif num.isnumeric() and (re.match(regex, content) or re.findall('spam', content.lower())):
        print("Fully Invalid")


n = input()
c = input()
spam(n, c)

# import re
#
# user = input()
# body = input()
#
# def isSpam(user, body):
#     l = len(body)
#     c1=user.isdigit()
#     s=body.replace(' ','')
#     s=re.sub('[\W_]','0',s)
#     c2=len(re.findall('0',s))>l/2 and len(re.findall('spam', body.lower())) != 0
#     if c1 and c2:
#         return 'Fully Invalid'
#     else:
#         if c1:
#             return 'Invalid Sender'
#         else:
#             if c2:
#                 return 'Invalid Content'
#             else:
#                 return 'Not Spam'
#
#
#
# print(isSpam(user, body))