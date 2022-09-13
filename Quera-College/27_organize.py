##سازماندهی رسانه
import datetime
import os
import sys


def media(src, dst):
    print("Last modified: %s" % (datetime.datetime.fromtimestamp(os.path.getctime(src))).strftime("%Y"))

    image = (".jpg", ".jpeg", ".png")
    video = (".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov")

    for folder, subfolders, filename in os.walk(src):
        print(filename)

        if any([filename.lower().endswith(tuple(image)) for filename in filename]):
            print("Last modified: %s" % (datetime.datetime.fromtimestamp(os.path.getctime())).strftime("%Y"))


#     file_dict = {}
#     for root, dirs, files in os.walk(src):
#         for file in files:
#             if file.lower().endswith(ttype.lower()):
#                 path = os.path.join(root)
#                 if path in file_dict:
#                     count = file_dict[path] + 1
#                     file_dict[os.path.join(root)] = count
#                 else:
#                     file_dict[os.path.join(root)] = count
#
#
# try:
#     os.mkdir(dst)
# except FileExistsError:
#     pass
#
#     return (file_dict)

media(sys.argv[1], sys.argv[2])
