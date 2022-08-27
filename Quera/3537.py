def Repet(number):
    x="W"
    for f in range(number):
        x +="o"
    x+="w!"
    return x

print(Repet(int(input())))
