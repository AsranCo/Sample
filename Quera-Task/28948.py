def typeist(x):
    result = []
    for f in x:
        if f == ('=') and len(result) != 0:
            result.pop()
        else:
            result.append(f)

    print(''.join(result))


typeist(list(input()))
