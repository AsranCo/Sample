##محاسبه‌گر
def calculator(n, m, ls):
    new_list = []
    count = 0
    t = 0
    m_0 = m
    for f in ls:
        t += f
        count += 1
        if count == m:
            m = m_0 + m
            new_list.append(t)
            t = 0
        elif count >= n:
            new_list.append(t)
    x = 0
    l = 1
    for i in range(len(new_list)):
        x = (new_list[i] * l) + x
        l = l * (-1)
    return (x)


# print(calculator(8,3, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
