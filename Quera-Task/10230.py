n, k, s = map(float, input().split())
if n == 0 or k == 0 or s == 0:
    print("No")
else:
    if (n + k + s) == 180:
        print("Yes")
    else:
        print("No")
