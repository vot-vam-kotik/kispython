def g1(x):
    return x + x


# Умножение на 12. 4 сложения.
def f1(x):
    return g1(x) + g1(x) + g1(g1(x)) + g1(g1(x))


def g3(x):
    return x + x + x


# Умножение на 16. 4 сложения.
def f2(x):
    return g1(g1(g1(x))) + g1(g1(x)) + g1(g1(x))


# Умножение на 15. 3 сложения и 2 вычитания.
def f3(x):
    a1 = g1(g1(g1(g1(g1(x))))) - g3(g3(x))
    a3 = g1(g1(g1(x)))
    return a1 - a3


# Умножение на 29. 6 сложений и одно вычитание.
def f4(x):
    return g1(g1(g1(x))) + g1(g1(g1(x))) + g1(g1(g1(x))) + g1(g1(g1(x))) - g3(x)


print(f1(2))
print(f2(2))
print(f3(2))