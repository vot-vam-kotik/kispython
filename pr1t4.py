def f_12_4(x):
    x += x
    x += x + x
    x += x
    return x


def f_16_4(x):
    x += x
    x += x
    x += x
    x += x
    return x


def f_15_3_2(x):
    y = x
    x = x + x
    x = x + x
    x = x + x
    y = y - x
    x = x - y
    return x


def f_29_6_1(x):
    a = x + x
    x = a + x
    a += a
    a += a
    a += a
    a += a
    a = a - x
    return a


print(f_12_4(2))
print(f_16_4(2))
print(f_15_3_2(2))
print(f_29_6_1(2))

