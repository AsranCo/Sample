##چاپ برعکس
result = []
while True:
    name = int(input())
    result.append(name)
    if name == 0:
        list.reverse(result)
        for f in range(1, len(result)):
            print(result[f])
        break
