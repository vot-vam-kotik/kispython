def main(x):
    a = 0b00000000000000000011111111111111
    b = 0b00000111111111111100000000000000
    c = 0b11111000000000000000000000000000

    a = x & a
    b = x & b
    c = x & c

    a = a << 18
    b = b >> 9
    c = c >> 27

    result = a + b + c
    return result


print(hex(main(0x38158b68)))