# task 2
# print (1/0)

# функция as_integer_ratio - возвраащет 2 значения
b = 3
print(b.as_integer_ratio())
print(42.0 == 42)
print(41.999999999999999 == 42)
print(41.9999999999999999888888888 == 42)
print(41.99999999999999900000000000 == 42)
print(42.000000000000001 == 42)
print(42.00000000000000 == 42)
print(42.000000000000000009999999 == 42)
print(0b101010 == 42)  # bin int
print(0o52 == 42)  # oct int
print(0x2a == 42)  # hex int

# пасхалки - https://tproger.ru/devnull/python-easter-eggs/

x=0
for i in range (0,4294967295):
    x += 4294967295