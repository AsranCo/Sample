def star():
    n, m = map(int, input().split())
    s = ""
    for i in range(n):
        s += input()
    print(s.count("*"))


star()
