# Реализовать классы Num, Add, Mul.


class Num:
    def __init__(self, number):
        self.number = number

    def stack(self):
        print('PUSH ' + str(self.number))

    def __repr__(self):
        return str(self.number)