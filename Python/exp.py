# def FirstCount(s):
#     res = list(map(int, str(s)))
#     for i in range(len(res)):
#         # print(res[i], ": ", int(res[i]).extend(i))
#         print(str(res[i]), ": ", str(res[i]) * res[i])
#     return str
#
# FirstCount(input())
# ----------------------------------------------------------
# def FirstReverse(s):
#     num = ""
#     for i in s:
#         print(i)
#         print(num)
#         num = i + num
#     return num
#
# print(FirstReverse(input()))
# ----------------------------------------------------------
def get_func(ls):
    # توابع محاسبه‌گر مساحت

    pass


ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

print(ls[0](1))  # 1
print(ls[1](2))  # 12.566370614359172
print(ls[2](2, 4))  # 8
print(ls[3](4, 5))  # 10.0
