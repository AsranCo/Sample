def Charge(s):
    t = ""
    for i in range(1, s + 1):
        t += str(i)
    print(t[int(s-1)])


Charge(int(input()))
