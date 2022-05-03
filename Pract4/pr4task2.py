'''Использование встроенных функций.

Напишите код, который выведет на экране все переменные объекта произвольного пользовательского класса.
Напишите код, который по имени метода, заданному строкой,
вызовет этот метод в объекте некоторого пользовательского класса.'''


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.__surname = surname
        self.__age = age

    def get_info(self):
        return 'Имя+Фамилия-> {} {}\nВозраст: {}'.format(str(self.name), str(self.__surname), str(self.__age))


print('Первая часть задания')
person = Person('Петя', 'Курочкин', 21)
print(vars(person))

print('\nВторая часть задания')
person = Person('Петя', 'Курочкин', 21)
method_to_invoke = getattr(person, 'get_info')
print(method_to_invoke())

