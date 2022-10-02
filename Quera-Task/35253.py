n = int(input())
x = map(int, input().split(maxsplit=n - 1))
x = list(x)
max_value = sorted(x)[-1]
print(x.index(max_value) + 1)

# n = int(input())
# w = [int(x) for x in input().split()]
# print(1 + w.index(max(w)))
