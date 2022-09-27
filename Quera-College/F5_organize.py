##سازماندهی رسانه
import datetime
import os
import sys


def media(src, dst):
    global address
    image = (".jpg", ".jpeg", ".png")
    video = (".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov")

    for folder, subfolders, filename in os.walk(src):
        for f in filename:
            if any([f.lower().endswith(tuple(video))]):
                filepath_video = (f"{folder}" + f"/{f}")
                modef_time = (datetime.datetime.fromtimestamp(os.path.getmtime(filepath_video))).strftime("%Y")
                try:
                    address = f"{dst}/{modef_time}/videos"
                    os.makedirs(address)
                    with open(filepath_video, 'rb') as firstfile, open(address + f"/{f}", 'wb') as secondfile:
                        for line in firstfile:
                            secondfile.write(line)
                except FileExistsError:
                    with open(filepath_video, 'rb') as firstfile, open(address + f"/{f}", 'wb') as secondfile:
                        for line in firstfile:
                            secondfile.write(line)

            if any([f.lower().endswith(tuple(image))]):
                filepath_image = (f"{folder}" + f"/{f}")
                modef_time = (datetime.datetime.fromtimestamp(os.path.getmtime(filepath_image))).strftime("%Y")

                try:
                    address = f"{dst}/{modef_time}/photos"
                    os.makedirs(address)
                    with open(filepath_image, 'rb') as firstfile, open(address + f"/{f}", 'wb') as secondfile:
                        for line in firstfile:
                            secondfile.write(line)
                except FileExistsError:
                    with open(filepath_image, 'rb') as firstfile, open(address + f"/{f}", 'wb') as secondfile:
                        for line in firstfile:
                            secondfile.write(line)


# media("./file/src", "./file/dst")
media(sys.argv[1], sys.argv[2])

#--------------------------------------- todo پاسخ دیکران
# import os
# import sys
# import re
# import time
#
#
# inputs = sys.argv
# src = inputs[1]
# dist = inputs[2]
# if not(os.path.isdir(dist)):
#     os.mkdir(dist)
#
# docs = os.walk(src)
#
# def makeDist(fileType, year , fileName):
#     fileAddr = os.path.join(dist, year)
#     if not(os.path.isdir(fileAddr)):
#         os.mkdir(fileAddr)
#     fileAddr = os.path.join(dist, year, fileType)
#     if not(os.path.isdir(fileAddr)):
#         os.mkdir(fileAddr)
#     fileAddr = os.path.join(dist, year, fileType , fileName)
#     return fileAddr
#
#
# for root, dirs, files in docs:
#     for fileName in files:
#         fileType = ""
#         if bool(re.match(".+\.(jpg|jpeg|png)$", fileName.lower())):
#             fileType = "photos"
#         elif bool(re.match(".+\.(mp4|avi|3gp|mpeg|mkv|wmv|mov)$", fileName.lower())):
#             fileType = "videos"
#         else:
#             continue
#         fileAddr = os.path.join(root, fileName)
#         year = time.ctime(os.path.getmtime(fileAddr)).split()[-1]
#         with open(fileAddr, 'rb') as src:
#             data = src.read()
#             with open(makeDist(fileType,year,fileName), 'wb') as dst:
#                 dst.write(data)
