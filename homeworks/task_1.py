from math import floor, sqrt


def main(y, z):
    a = (y ** 3 - 36 * y - 53) ** 5 + (y ** 2 + 1 + 30 * z) ** 7
    b = (54 * (41 - z - y ** 3 / 59) ** 3 - 0.02)
    return z ** 7 - y ** 4 / 92 + sqrt(a / b)

f = main(0.66, 0.94)
print(f"{f:.2e}")