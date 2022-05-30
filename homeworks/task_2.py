from math import log, fabs


def main(x):
    if x < 98:
        return 92 * x ** 6 + 4
    elif x < 122:
        return x ** 2 / 27
    elif x < 169:
        return 83 * (fabs(x ** 3 / 34) ** 3) +\
            15 * log(x) ** 6 + \
            log(65 + 11 * x ** 3 + x) ** 2
    elif x < 266:
        return 22 * x ** 4 + x +\
               (x - x ** 3 - 23 * x ** 2) ** 3
    else:
        return 78 * x ** 7 - x ** 5


# --- cut this out when submitting to robot ---
f = main(251)
print(f"{f:.2e}")