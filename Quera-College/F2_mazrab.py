##کوچک‌ترین مضرب
def Mza():
    p, d = map(int, input().split())

    while True:

        if 0 <= d % p <= p / 2:
            print(d)
            break
        else:
            d = d + d
            continue


Mza()
