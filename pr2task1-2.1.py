# Преобразовать элементы списка s из строковой в числовую форму
def to_nums(s):
    return [float(i) for i in s]


# Подсчитать количество различных элементов в последовательности s
def find_uniques(s):
    return len(set(s))


# Обратить последовательность s без использования функций
def reverse_list(s):
    return s[::-1]

# Выдать список индексов, на которых найден элемент x в последовательности s
def get_index_of_equal_to_x(x,s):
    return [i for i in range(len(s)) if s[i] == x]


# Сложить элементы списка s с четными индексами
def sum_even_index(s):
    return sum(s[0::2])


# Найти строку максимальной длины в списке строк s
s = ['0.49', '0.54', '0.54', '0.55', '0.55555', '0.54', '0.55', '0.55', '0.54']
def find_max_len_elem(s):
    return max(s, key=len)



if __name__ == '__main__':
    assert to_nums(['0.49', '0.54', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']) == [0.49, 0.54, 0.54, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54]
    assert find_uniques([1, 4, 5, 7, 4, 3, 6, 7]) == 6
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert get_index_of_equal_to_x(5, [5, 1, 2, 5, 3, 4, 5]) == [0, 3, 6]
    assert sum_even_index([2, 1, 2, 1, 2, 1, 2]) == 8
    assert find_max_len_elem(['0.49', '0.54', '0.54', '0.55', '0.55555', '0.54', '0.55', '0.55', '0.54']) == '0.55555'

i = 1
#['much', 'code', 'wow'][i] - было

print('mucucocewhw'[::i+3])