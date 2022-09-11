def ColHeat(num):
    x = input().split(maxsplit=num)

    for i in range(num):
        if int(x[i]) > 15:
            print("cooler")
        else:
            print("heater")

ColHeat(int(input()))
