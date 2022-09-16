
import re


def real_numbers(numbers):
    regex = '^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$'
    real_listp=[]
    for i in numbers:
        if re.match(regex, i):
            real_listp.append("LEGAL")
        else:
            real_listp.append("ILLEGAL")
    return real_listp

real_numbers(input())