#چاپگر
n, m = map(int, input().split())
x = "X" * m
d = "." * m

line = x + d + x
middleLine = d + x + d
for ii in range(n):
    print(line)
for b in range(n):
    print(middleLine)
for ii in range(n):
    print(line)
