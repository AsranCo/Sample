def Diamond(num):
    for i in range(1, num + 1):
        i = i - (num // 2 + 1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (num - i * 2) + " " * i+" " * i + "*" * (num - i * 2) + " " * i)


Diamond(int(input()))
