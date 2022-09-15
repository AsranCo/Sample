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
# import sys
# import os
# import time
#
# videoFormats = (".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov")
# imageFormats = (".jpg", ".jpeg", ".png")
#
#
# def isVideo(file):
#     return file.lower().endswith(videoFormats)
#
# def isImage(file):
#     return file.lower().endswith(imageFormats)
#
# def makeDir(path):
#     if not os.path.isdir(path):
#         os.mkdir(path)
#
# def copy_file(file_address, file, path):
#     with open(file_address, 'rb') as src:
#         data = src.read()
#         with open(os.path.join(path, file), 'wb') as dst:
#             dst.write(data)
#
# def organize():
#     origin, destination = sys.argv[1], sys.argv[2]
#     makeDir(destination)
#
#     for dirpath,_,files in os.walk(origin):
#         for file in files:
#             file_address = os.path.join(dirpath, file)
#             seconds = os.path.getmtime(file_address)
#             year = time.ctime(seconds)[-4:]
#
#             if isVideo(file):
#                 print(os.path.join(destination, year, 'videos', file))
#                 makeDir(os.path.join(destination, year))
#                 makeDir(os.path.join(destination, year, 'videos'))
#                 copy_file(file_address, file, os.path.join(destination, year, "videos"))
#             elif isImage(file):
#                 print(os.path.join(destination, year, 'photos', file))
#                 makeDir(os.path.join(destination, year))
#                 makeDir(os.path.join(destination, year, 'photos'))
#                 copy_file(file_address, file, os.path.join(destination, year, "photos"))
#
# organize()