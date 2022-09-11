n = int(input())
x = " "
for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(n):
            print("*", end='')
        print()
    else:
        print("*", f"{(n-4) * x}", "*")

print()
