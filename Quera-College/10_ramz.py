##رمز
rang = int(input())
ramz = input()

li = []
c = 0
for f in range(rang):
    li.append(str(input()))
for i in range(len(ramz)):
    if li[i].find(ramz[i]) > 4:
        c = c + (9 - li[i].find(ramz[i]))
    else:
        c = c + li[i].find(ramz[i])
print(c)
