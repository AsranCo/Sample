def Hard(s):
    g = 0
    y = 0
    r = 0
    for f in range(5):
        if str(s[f]) == "G":
            g += 1
        elif str(s[f]) == "Y":
            y += 1
        else:
            r += 1

    if r >= 3 or g == 0:
        print("nakhor lite")
    elif r >= 2 and y >= 2:
        print("nakhor lite")
    else:
        print("rahat baash")


Hard(input())
