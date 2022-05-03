'''Для программы с классами используйте инвариант inv.
Реализуйте контракт, выполнение которого deal проверяет статически.
Какие ограничения имеют статически проверяемые контракты?'''


import deal
@deal.inv(lambda account: account.money >= 0)
class Account:
    def __init__(self):
        self.money = 0

    def get(self, amount):
        self.money -= amount

    def put(self, amount):
        self.money += amount


a = Account()

a.put(10)
a.get(10)
# Раскомментируйте следующую строку, чтобы получить ошибку контракта
# a.money -= 20
a.money