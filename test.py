# from datetime import date, datetime
#
#
# def day_calculator(n):
#     sajjad_bdate = date(1999, 1, 14)
#     birthday = n.split("-")
#     bi = date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
#     age = (bi - sajjad_bdate).days
#     if int(age) > 0:
#         return (age)
#     else:
#         return ("Not yet born")


# def karim(n):
#     x = []
#     l = []
#     for f in range(n):
#         x.append(str(input()))
#     for i in range(n):
#         l.append(len(set(x[i])))
#     l.sort()
#     print(l[-1])
#
#
# karim(int(input()))


# rang = int(input())
# ramz = input()
#
# li = []
# c = 0
# for f in range(rang):
#     li.append(str(input()))
# for i in range(len(ramz)):
#     if li[i].find(ramz[i]) > 4:
#         print(9 - li[i].find(ramz[i]))
#         c = c + (9 - li[i].find(ramz[i]))
#     else:
#         print( li[i].find(ramz[i]))
#         c = c + li[i].find(ramz[i])
# print(c)
#




print(str("{:b}".format(int(input()))).count("1"))

