from math import ceil, sqrt


def main(y, z):
    sum_i = 0
    for i in range(1, len(z)+1):
        a = 74 * y[ceil(i / 2 - 1)] ** 2
        b = 26 * z[ceil(i / 2 - 1)] ** 3
        sum_i += 22 * ((sqrt(a - b - 0.02)) ** 6)
    return sum_i


f= main([-0.67, -0.33],[0.24, -0.59])
print(f"{f:.2e}")

'''

def main (v2_y, v2_z):
    sum_i = decimal.Decimal(0);
    for i in range(1, len(v2_z) + 1):
        y_i = decimal.Decimal(v2_y[ceil(i / 2 - 1)])
        z_i = decimal.Decimal(v2_z[ceil(i / 2 - 1)])
        sum_i += decimal.Decimal(22) * (decimal.Decimal(74) * y_i.__pow__(2) - decimal.Decimal(26) * z_i.__pow__(3) - decimal.Decimal("0.02")).__pow__(3)
    return sum_i

f= main(["-0.67", "-0.33"],["0.24", "-0.59"])
print(f"{f:.2e}")
'''