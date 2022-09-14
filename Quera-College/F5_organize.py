##سازماندهی رسانه
import datetime
import os
import sys


def media(src, dst):
    image = (".jpg", ".jpeg", ".png")
    video = (".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov")

    for folder, subfolders, filename in os.walk(src):
        for f in filename:
            if any([f.lower().endswith(tuple(video))]):
                filepath_video = (f"{folder}" + f"/{f}")
                modef_time = (datetime.datetime.fromtimestamp(os.path.getctime(filepath_video))).strftime("%Y")
                try:
                    os.makedirs(f"{dst}/{modef_time}/photos")
                except FileExistsError:
                    pass

            if any([f.lower().endswith(tuple(image))]):
                filepath_image = (f"{folder}" + f"/{f}")
                modef_time = (datetime.datetime.fromtimestamp(os.path.getctime(filepath_image))).strftime("%Y")
                try:
                    print(dst)
                    os.makedirs(f"{dst}/{modef_time}/videos")
                except FileExistsError:
                    pass


media("./file/src", "./file/dst")
# media(sys.argv[1], sys.argv[2])
