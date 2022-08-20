import time
import random
import concurrent.futures

figures = [random.randint(1, 5000000) for i in range(0, 1000)]  # Generating random figures


def print_figure(figure):
    print(figure)
    time.sleep(1)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for figure in figures:
            executor.submit(print_figure, figure)  # You can pass as many arguments as you want


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

# ------------------------------------------------- insert to sqlite3
import os
import sqlite3
import urllib.request
import concurrent.futures

def download_file(file_url, dst_file):
    if not file_url:
        print(f"Empty file {dst_file}")
        return
    if not os.path.exists(dst_file):
        try:
            print(f"Downloading {dst_file}")
            urllib.request.urlretrieve(file_url, dst_file)
        except Exception as e:
            print(e)
            print(f"Failed to retrieve {dst_file}'s file")
    return

def main():
    connection = sqlite3.connect("my_sqlite.db")
    cursor = connection.cursor()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for row in cursor.execute('SELECT * FROM users;'):
            user_id = row[0]
            file_url = row[1]
            dst_file = f"./files/{str(user_id)}.jpg"
            executor.submit(download_file, file_url, dst_file)
    connection.close()

if __name__ == "__main__":
    main()