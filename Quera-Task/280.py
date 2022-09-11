list_num = []
for i in range(3):
    s = int(input())
    list_num.append(s)
list_num.sort()
if list_num[2] != 0 and list_num[1] != 0 and list_num[0] != 0:
    if ((list_num[2]) ** 2) == ((list_num[1]) ** 2 + (list_num[0]) ** 2):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
