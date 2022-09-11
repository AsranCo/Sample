def EX(n):
    m = 1
    while n >= m:
        for i in range(1, n + 1):
            print(i * m, end=' ')
        print()
        m = m + 1


EX(int(input()))