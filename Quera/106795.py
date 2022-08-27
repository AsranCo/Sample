list_num = []
for i in range(2):
    s = input()
    list_num.append(s)

if (str(list_num[0])[0] == str(list_num[1])[-1]):
    print("YES")
else:
    print("NO")
