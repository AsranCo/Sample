##جستوجوگر

import os


def explore(ttype, address):
    file_dict = {}
    for root, dirs, files in os.walk(address):
        count = 1
        for file in files:
            if file.lower().endswith(ttype.lower()):
                path = os.path.join(root)
                if path in file_dict:
                    count = file_dict[path] + 1
                    file_dict[os.path.join(root)] = count
                else:
                    file_dict[os.path.join(root)] = count

    return (file_dict)


print(explore("xml", "/home/ali/snap"))
