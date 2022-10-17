def Diamond(num):
    s=num*2+1
    for i in range(1, s + 1):
        i = i - (s // 2 + 1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (s - i * 2) )

Diamond(int(input()))
