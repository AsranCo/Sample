import threading, time
from threading import Thread


def f():
    t1 = Thread(name=1, target=functions.f[0])
    t2 = Thread(name=2, target=functions.f[0])
    t3 = Thread(name=3, target=functions.f[0])
    t4 = Thread(name=4, target=functions.f[0])


t = Thread(target=f)
t.start()
t.join()
print('salam')
print(t.is_alive())
print("---------------------")

t = Thread(target=f)
t.start()
t.join(1.0)
print('khoobi?')
print(t.is_alive())
print("---------------------")

t = Thread(target=f)
t.start()
print('che khabar?')
print(t.is_alive())
print("---------------------")
