'''Реализуйте структуру данных хэш-таблицу, аналог встроенного dict.
 Используйте список пар ключ-значение. Примените тестирование на случайных данных с использованием assert и dict.
Реализуйте методы чтения, записи, получения размера хэш-таблицы.
Сделайте вышеупомянутые методы операторами/функциями, по аналогии с dict.
Реализуйте поддержку итератора для цикла for. '''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.size = 0
        self.n = 0
        self.buckets = [None] * self.capacity

    def hash(self, key): # хэш-функция
        return hash(key) % self.capacity

    def get(self, key):   # поиск элемента по значению в ключе
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def add(self, key, value):  # добавление элемента
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(key, value)

    def remove(self, key): # удаление всех элемнтов по ключу
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        result = node.value

        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = prev.next.next

        self.size -= 1
        return result

    def size(self):
        return self.size

    def __next__(self):  # переход к следующему элементу хэш-таблицы
        if self.n is not None:
            current = self.n
            self.n = self.n.next
            return current.key, current.value

        self.b += 1
        if self.b == self.capacity:
            raise StopIteration
        self.n = self.buckets[self.b]

        return self.__next__()

    def __iter__(self):
        self.b = 0
        self.n = self.buckets[0]
        return self

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __len__(self):
        return self.size


def test_hash_table():
    print('Тесты хэш-таблицы')
    table = HashTable()

    for i in range(50):
        table[i] = i + 1
        assert table[i] == i + 1

    assert len(table) == 50
2
    for key, value in table:
        print(str(key) + ': ' + str(value))


test_hash_table()