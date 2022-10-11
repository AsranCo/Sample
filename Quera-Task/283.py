a = int(input())
b = int(input())
if b >= a:
    print("Wrong order!")
elif (a - b) % 2 != 0:
    print("Wrong difference!")
else:

    for i in range(a):
        for j in range(a):
            if ((a - b) / 2) < i+1  and ((a - b) / 2) > i-b and ((a - b) / 2) > j-b and ((a - b) / 2) < j+1:
                print("  ", end='')
                # print("* ",end='')
            else:
                print("* ", end='')

        print("")

