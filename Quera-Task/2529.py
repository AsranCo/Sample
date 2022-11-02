def karim(n):
    x = []
    l = []
    for f in range(n):
        x.append(str(input()))
    for i in range(n):
        l.append(len(set(x[i])))
    l.sort()
    print(l[-1])


karim(int(input()))