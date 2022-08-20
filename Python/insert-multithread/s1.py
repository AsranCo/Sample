import os
import time
import sqlite3
import threading


conn = None


def create_table():
    global conn
    try:
        os.remove("foo.db")
    except OSError:
        pass
    conn = sqlite3.connect("foo.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("""CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)""")


def writer_thread():
    writer = conn.cursor()
    for i in range(100000):
        writer.execute("INSERT INTO test (name) VALUES (?)", (str(i),))
    print("Writer done")


def reader_thread():
    reader = conn.cursor()
    count = 0
    for i in range(10):
        for row in reader.execute("SELECT * FROM test"):
            count += 1
    print ("Reader done, num_rows seen:", count)


# Single threaded.
print( "Single threaded, write 100000, read all records 10 times")
start = time.time()
create_table()
writer_thread()
for i in range(10):
    reader_thread()
end = time.time()
print( "Total single threaded: %.4f" % (end - start))
## Used for sanity check later.
first_result = list(conn.execute("SELECT * FROM test"))

# Threaded version.
print( "\nMulti threaded, write 100000, read all records 10 times, all in separate threads.")
start = time.time()
create_table()

write = threading.Thread(target=writer_thread)
readers = [threading.Thread(target=reader_thread) for i in range(10)]

write.start()
[r.start() for r in readers]

write.join()
[r.join() for r in readers]
end = time.time()
print( "Total multi threaded: %.4f" % (end - start))
# Double check we aren't getting any different results
# in the final result between single threaded and multithreaded
# versions.
second_result = list(conn.execute("SELECT * FROM test"))
assert first_result == second_result