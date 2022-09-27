##جستوجوگر

import os


def explore(ttype, address):
    file_dict = {}
    for root, dirs, files in os.walk(address):
        count = 1
        for file in files:
            # if file.lower().endswith(ttype.lower()):
            if file.endswith(ttype.lower()):
                path = os.path.join(root)
                if path in file_dict:
                    count = file_dict[path] + 1
                    file_dict[os.path.join(root)] = count
                else:
                    file_dict[os.path.join(root)] = count

    return (file_dict)


print(explore("xMl", "/home/ali/snap"))
# --------------------------------------------------------------todo پاسخ دیگران
# import os
#
# def explore(extension, addr):
#     result = dict()
#     for obj in os.walk(addr):
#         for name in obj[2]:
#             if "." in name and name.split('.')[-1].lower() == extension.lower():
#                 try:
#                     result[obj[0]] += 1
#                 except KeyError:

#                     result[obj[0]] = 1
#     return result