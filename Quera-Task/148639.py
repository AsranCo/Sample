def add_next(N, bits):
    if bits == 1:
        return [""]
    ret = []
    c = 2 ** (N - 1)
    if N == bits:
        while c < 2 ** N - 1:
            ret.append("+\\frac{" + str(c) + "}{" + str(c + 1) + "}")
            c = c + 2
    else:
        add = add_next(N + 1, bits)
        while c < 2 ** N - 1:
            a = str(add[c - 2 ** (N - 1)])
            b = str(add[c - 2 ** (N - 1) + 1])
            ret.append("+\\frac{" + str(c) + a + "}{" + str(c + 1) + b + "}")

            c = c + 2

    return ret


bits = int(input(""))

m = "1"+add_next(2, bits)[0]
print(m)