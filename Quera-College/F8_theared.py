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

# -------------------------------------------------------

# from threading import Thread
#
#
# def sol(func):
#     threads = []
#     for i in range(len(func)):
#         threads.append(Thread(target = func[i], name = str(i + 1)))
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#
#
# def solve():
#     sol(functions.f)
#     sol(functions.g)
#     sol(functions.h)
#
