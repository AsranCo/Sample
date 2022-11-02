import math

n, k = map(int, input().split())
for i in range(k):
    n = n / 2
print(math.floor((n)))
