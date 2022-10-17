import threading, time
from threading import Thread


def solve(functions):
    f = None
    for i in range(3):
        f = Thread(name=i, target=functions.f[i])
        f.start()
        f.join()
    if f.is_alive():
        pass
    else:
        for i in range(1):
            g = Thread(name=i, target=functions.f[i])
            g.start()
            g.join()
        if g.is_alive():
            pass
        else:
            h = Thread(name=i, target=functions.f[i])
            h.start()
            h.join()
