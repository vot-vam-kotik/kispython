from Pract4.pr3task4.Operation import Operation
# Реализовать классы Num, Add, Mul.

class Add(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.number = int(self.num1.number + self.num2.number)

    def count(self):
        return self.number

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('ADD')

    def __repr__(self):
        return '({} + {})'.format(self.num1, self.num2)
