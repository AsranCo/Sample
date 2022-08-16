import os


def get_all_files_of_extension():
    directory = "/home/ali/snap/"
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xml") and (not file.startswith("org")):
                file_list.append(os.path.join(root, file))

    return file_list


try:
    get_all = get_all_files_of_extension()
    for f in get_all:
        print(f)
except Exception as e:
    print("Error  ->> " + str(e))
