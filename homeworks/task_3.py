from math import log10


def main(m, n, b):
    sum_j = 0
    for c in range(1, b + 1):
        for k in range(1, n + 1):
            for j in range(1, m + 1):
                sum_j += log10(c) ** 5 + (k - 59 * j ** 2) / 61
    return sum_j


# --- cut this out when submitting to robot ---
print(f"{main(8, 5, 4):.2e}")
# -3.45e+02
