def keyb(num):
    res = ""
    cap = 1
    for i in range(num):
        a = input()
        if a == "CAPS":
            cap *= -1
        if cap == -1 and not a == "CAPS":
            res += a.upper()
        elif a != "CAPS":
            res += a
    print(res)


keyb(int(input()))
