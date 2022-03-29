from my_package.my_module import Calculator, Joiner

calculator = Calculator()
print(calculator.divide(2, 1))
print(calculator.divide(2, 0))

joiner = Joiner()
print(joiner.join('1', '1'))
print(joiner.join('1', 1))