def find(num1, num2, num3):
    a = [1, 2, 3, 4]
    b = [num3, num2, num1]

    return (set(a).difference(set(b))).pop()
