import functions
from threading import Thread


def sol(func):
    threads = []
    for i in range(len(func)):
        threads.append(Thread(target = func[i], name = str(i + 1)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def solve():
    sol(functions.f)
    sol(functions.g)
    sol(functions.h)