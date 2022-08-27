def Reverse(num):
    x = input().split(maxsplit=num)
    str(x.reverse())
    for i in range(num):
        print(x[i], end=" ")


Reverse(int(input()))
