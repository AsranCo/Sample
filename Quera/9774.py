def FirstCount(s):
    res = list(map(int, str(s)))
    for i in range(len(res)):
        # print(res[i], ": ", int(res[i]).extend(i))
        print(f"{str(res[i])}:", str(res[i]) * res[i])
    return str

FirstCount(input())