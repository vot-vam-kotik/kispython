def fast_pow(x, y):
    res = 1
    while y >= 1:
        if y % 2 != 0:
            res *= x
        x *= x
        y //= 2
    return res


def test():
    for x in range(0, 101):
        for y in range(0, 101):
            assert fast_pow(x, y) == pow(x,y)
    print("pow is correct")


test()
