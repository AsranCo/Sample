from threading import Thread, Lock


def synchronized(func):
    def wrapper(self, *args, **kwargs):
        self.lock.acquire()
        r = func(self, *args, **kwargs)
        self.lock.release()
        return r

    return wrapper


a = 0


@synchronized
def f():
    global a
    for i in range(300000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)
t.start()
s.start()

# synchronized = synchronized(s.join())

print(" *** ", a)
