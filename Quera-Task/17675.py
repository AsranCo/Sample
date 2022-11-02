def fib():
    n = input()

    a = [0, 1]
    b = [i for i in range(1, int(n) + 1)]
    result = ""
    while int(n) + 1 > len(a): a.append(a[-1] + a[-2])

    for f in range(int(n)):
        if b[f] in a:
            result += ("+")
        else:
            result += ("-")

    print(result)


fib()
