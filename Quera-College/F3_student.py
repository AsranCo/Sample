##دانشجویان بی‌کار
import re


def solve(arr):
    global y
    if re.search('(\d+)#(\d+)', arr):
        z = re.search('(\d+)#(\d+)', arr)[0]
        x = re.sub('(\d+)#(\d+)', "x", arr)
    elif re.search('#(\d+)', arr):
        z = (re.search('#(\d+)', arr)[0])
        x = re.sub('#(\d+)', "x", arr)
    elif (re.search('(\d+)#', arr)):
        z = (re.search('(\d+)#', arr)[0])
        x = re.sub('(\d+)#', "x", arr)
    else:
        z = (re.search('#', arr)[0])
        x = re.sub('#', "x", arr)

    eq = x.split("=")[-1].replace(" ", "")
    s1 = x.split("+")[0].replace(" ", "")
    s2 = x.split("+")[1].split("=")[0].replace(" ", "")

    if eq == "x":
        y = int(s1) + int(s2)

    elif s1 == "x":
        y = int(eq) - int(s2)

    elif s2 == "x":
        y = int(eq) - int(s1)
    step = (z.find("#")) + 1
    resu = ""

    for i in range(y + 2):

        x1 = (z.replace("#", ('{:0{}d}'.format(i, 3))))
        if str(y) == x1:
            resu = (x.replace("x", str(x1)))
            break

    if resu != "":
        return (resu)
    else:
        return ("-1")

    # --------------------------------------------------#

    # def solve(string):
    #
    # import re
    # x = re.findall('[0-9]*#[0-9]*', string)[0]
    # regex = '^' + x.replace('#', '.*') + '$'
    # new_string = string.replace(x, '')
    # a, b = int(re.findall('[0-9]+', new_string)[0]), int(re.findall('[0-9]+', new_string)[1])
    # number1 = b - a
    # number2 = a + b
    # if re.match(r'.+=\s?[0-9]+$', new_string) and re.match(regex, str(number1)):
    #     return re.sub('[0-9]*#[0-9]*', str(number1), string)
    # elif re.match(r'.+=\s?$', new_string) and re.match(regex, str(number2)):
    #     return re.sub('[0-9]*#[0-9]*', str(number2), string)
    # else:
    #     return '-1'
###############################################################