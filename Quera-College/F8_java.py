from threading import Thread, Lock, currentThread


def synchronized(f):
    lock = Lock()

    def wrapper(*args, **kwargs):
        lock.acquire()
        test = f(*args, **kwargs)
        lock.release()
        return test

    return wrapper


a = 0


@synchronized
def f():
    global a
    for i in range(400000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)

t.start()
s.start()

t.join()
s.join()

print(a)