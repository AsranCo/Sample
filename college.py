###############################################################
# words = [['s', 'a', 'l', 'a', 'm'], ['k', 'h', 'o', 'o', 'b', 'i', '?']]
#
# # for word in words:
# for char in words:
#     print(char, end='')
# print()

###############################################################
# def Zarb(n):
#     m = 1
#     while n >= m:
#         for i in range(1, n + 1):
#             print(i * m, end=' ')
#         print()
#         m = m + 1
#
#
# Zarb(int(input()))

###############################################################
# def Mazrab():
#     p, d = map(int, input().split())
#     while True:
#         if 0 <= d % p <= p / 2:
#             print(d)
#             break
#         else:
#             d += d
#             continue
#
#
# Mazrab()

###############################################################


# s = list()
# while (s2 := input()) != "test":
#     s.append(s2)
#     print(s)

# import math
#
# n = 9
# k = 4
# result = math.comb(n, k)
# print('comb(n, k) :', result)
###############################################################
# import math
# x = int(input())
# y = math.ceil(math.pow(x, 5/3) + math.tan(math.radians(x)))
# z = math.floor(math.pow(math.pi, (2 + math.atan(math.pow(math.sin(math.radians(x)), 2)))))
# print(math.gcd(y, z))

###############################################################

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
###############################################################
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


###############################################################
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
###############################################################
# print(str("{:b}".format(int(input()))).count("1"))
###############################################################بِسَنج!


# import re
#
#
# def validate_email(email):
#     regex = r'\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{3}\b'
#     if (re.fullmatch(regex, email)):
#         return True
#     else:
#         return False
#
#
# def validate_phone(number):
#     regex = r'^(?:09|\+989|00989)?(\d{9})$'
#     if (re.fullmatch(regex, number)):
#         return True
#     else:
#         return False
###############################################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import re
# def solve(arr):
#     global y
#     if re.search('(\d+)#(\d+)', arr):
#         z = re.search('(\d+)#(\d+)', arr)[0]
#         x = re.sub('(\d+)#(\d+)', "x", arr)
#     elif re.search('#(\d+)', arr):
#         z = (re.search('#(\d+)', arr)[0])
#         x = re.sub('#(\d+)', "x", arr)
#     elif (re.search('(\d+)#', arr)):
#         z = (re.search('(\d+)#', arr)[0])
#         x = re.sub('(\d+)#', "x", arr)
#     else:
#         z = (re.search('#', arr)[0])
#         x = re.sub('#', "x", arr)
#
#     eq = x.split("=")[-1].replace(" ", "")
#     s1 = x.split("+")[0].replace(" ", "")
#     s2 = x.split("+")[1].split("=")[0].replace(" ", "")
#
#     if eq == "x":
#         y = int(s1) + int(s2)
#
#     elif s1 == "x":
#         y = int(eq) - int(s2)
#
#     elif s2 == "x":
#         y = int(eq) - int(s1)
#     step = (z.find("#")) + 1
#     resu = ""
#
#     for i in range(y + 2):
#
#         # for num in range(y + 1):
#         x1 = (z.replace("#", ('{:0{}d}'.format(i, 4))))
#         if str(y) == x1:
#             resu = (x.replace("x", str(x1)))
#             break
#
#     if resu != "":
#         return (resu)
#     else:
#         return ("-1")
# ------------------------------------
# def solve(string):
#     import re
#     x = re.findall('[0-9]*#[0-9]*', string)[0]
#     regex = '^' + x.replace('#', '.*') + '$'
#     new_string = string.replace(x, '')
#     a, b = int(re.findall('[0-9]+', new_string)[0]), int(re.findall('[0-9]+', new_string)[1])
#     number1 = b - a
#     number2 = a + b
#     if re.match(r'.+=\s?[0-9]+$', new_string) and re.match(regex, str(number1)):
#         return re.sub('[0-9]*#[0-9]*', str(number1), string)
#     elif re.match(r'.+=\s?$', new_string) and re.match(regex, str(number2)):
#         return re.sub('[0-9]*#[0-9]*', str(number2), string)
#     else:
#         return '-1'
#
#
# print(solve("40838457 + 52979783 = #"))

###############################################################

# def type(x):
#     result = []
#     for f in x:
#         if f.startswith('=') and len(result) != 0:
#             result.pop()
#         else:
#             result.append(f)
#     print(''.join(result))
#
#
# type(str(input()))

###############################################################

#
# def creat_game(m, k, b):
#     map = []
#     for x in range(m):
#         map.append([])
#         for y in range(k):
#             map[x].append(0)
#     for l in b:
#         map[l[0] - 1][l[1] - 1] = "*"
#     return map
#
#
# def show_game(cre):
#     for row in cre:
#         show = ""
#         for col in row:
#             show += str(col) + " "
#         print(show)
#
#
# def calc_mine(m, k, map_game):
#     for i in range(m):
#         for j in range(k):
#             if map_game[i][j] == 0:
#                 count_bomb = 0
#                 try:
#                     if map_game[i][j - 1] == "*" and j != 0: count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i + 1][j - 1] == "*" and not j == 0: count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i + 1][j + 1] == "*": count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i][j + 1] == "*": count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i - 1][j] == "*" and not i == 0: count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i + 1][j] == "*": count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i - 1][j - 1] == "*" and j != 0 and i != 0: count_bomb += 1
#                 except:
#                     pass
#                 try:
#                     if map_game[i - 1][j + 1] == "*" and not i == 0: count_bomb += 1
#                 except:
#                     pass
#                 map_game[i][j] = count_bomb
#     return map_game
#
#
# m, k = map(int, input().split())
# b = int(input())
# mine_list = []
# for i in range(b):
#     row, col = map(int, input().split())
#     mine_list.append([row, col])
# map_game = creat_game(m, k, mine_list)
#
# final_game = calc_mine(m, k, map_game)
# show_game(final_game)
#
###############################################################

# print(*(sorted(x for x in list(map(int, input().split()))[5::6] if x % 6 == 0)))

###############################################################
# def calc(a):
#     avg, max = 0, 0
#     a = sorted(a)
#     c = len(a)
#     max = a[-1]
#     if len(a) % 2 == 0:
#         median = ((a[int((c / 2) + 1) - 1]) + (a[int((c / 2) - 1)])) / 2
#     else:
#         median = a[int((len(a) + 1) / 2) - 1]
#     for f in range(len(a)):
#         avg += a[f]
#     # def calc(a):
#     #     a.sort()
#     #     if len(a) % 2 == 0:
#     #         median = (a[int(len(a) / 2)] + a[int(len(a) / 2 - 1)]) / 2
#     #     else:
#     #         median = a[int(len(a) / 2)]
#     #     maximum = max(a)
#     #     average = sum(a) / len(a)
#     return (average, median, maximum)

###############################################################

# count_person = int(input())
# name_dict = {}
#
# for i in range(count_person):
#     name, family = map(str, input().split())
#     count_name = 1
#     if name in name_dict:
#         count_name = name_dict[name] + 1
#
#     name_dict[name] = count_name
# print(max(name_dict.values()))

###############################################################
# ^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$
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

# import re

#
# def check_registration_rules(**register):
#     password_regex = r'(?![0-9]+$)[A-Za-z0-9@#$%^&+=]{6,}'  ## not only number(?![0-9]+$) and min len {6,}
#     name_regex = r'[A-Za-z0-9@#$%^&+=]{4,}'
#     dic = []
#
#     for name, password in register.items():
#         # if (re.fullmatch(password_regex, password)) and (re.fullmatch(name_regex,
#         #                                                               name)) and (name != "quera") and (
#         #         name != "codecup"):
#         if len(password) >= 6 and len(name) >= 4 and name != "quera" and name != "codecup" and not str(
#                 password).isnumeric():
#             dic.append(name)
#     # print(dic)
#     return dic

# check_registration_rules(quera='qwerty80', mmdre/za='monday80', ali="aliali@", mammad="salam", saeed='1234567',
#                          ab='afj$L12', odecup='1234d56', sadegh='He3@lsa', alireza='ali669', username='password',
#                          sadeegh='He3@lsa')
###############################################################
# all_users = {}
# all_albums = {}
#
#
# def add_user(username, age, city, albums, all_users, all_albums):
#     pass
#
#
# def add_album(name, artist_name, genre, tracks, all_users, all_albums):
#     pass
#
#
# def query_user_artist(username, artist_name, all_users, all_albums):
#     pass
#
#
# def query_user_genre(username, genre, all_users, all_albums):
#     pass
#
#
# def query_age_artist(age, artist_name, all_users, all_albums):
#     pass
#
#
# def query_age_genre(age, genre, all_users, all_albums):
#     pass
#
#
# def query_city_artist(city, artist_name, all_users, all_albums):
#     pass
#
#
# def query_city_genre(city, genre, all_users, all_albums):
#     pass
#
#
# add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users, all_albums)

###############################################################
# def divs(n):
#     for i in range(1, n + 1):
#         if n % i == 0:
#             yield i
#
#
# print(list(divs(15)))


###############################################################
# def solve(path):
#     lines = []
#     count = 0
#
#     with open(path, "r") as f:  # after read file -> close file!
#         while True:
#             line = f.readline()
#             if line == '':
#                 break  # end of file
#             lines.append(line)
#
#     for line in lines:
#
#         count += 1
#         if line.startswith("#") or line.startswith(" ") or line.isspace():
#             count -= 1
#     return count
#
#
# print(solve("./text.info"))
###############################################################
