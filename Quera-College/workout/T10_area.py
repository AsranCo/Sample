import math


# def get_func(ls):
#     list = []
#     for item in ls:
#         if item == "square":
#             def f(x):
#                 return x * x
#
#             list.append(f)
#         elif item == "circle":
#             def f(x):
#                 return math.pi * x * x
#
#             list.append(f)
#         elif item == "rectangle":
#             def f(x, y):
#                 return x * y
#
#             list.append(f)
#         elif item == "triangle":
#             def f(x, y):
#                 return x * y / 2
#
#             list.append(f)
#
#     return list
#
#
# def get_func(ls):
#     for i, s in enumerate(ls):
#         if s == "square":
#             ls[i] = lambda x: x * x
#         if s == "circle":
#             ls[i] = lambda r: r * r * math.pi
#         if s == "rectangle":
#             ls[i] = lambda x, y: x * y
#         if s == "triangle":
#             ls[i] = lambda h, a: h * a / 2
#
#     return ls
#
#
# def get_func(arr):
#     switcher = {
#         "square": lambda x: x * x,
#         "circle": lambda x: x ** 2 * math.pi,
#         "rectangle": lambda x, y: x * y,
#         "triangle": lambda x, y: x * y * 0.5,
#     }
#     return [switcher.get(shape) for shape in arr]
#
# ------------------------------------------
#