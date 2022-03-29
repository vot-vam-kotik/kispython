# Существует модуль tabulate для вывода ASCII-таблиц.
# Это большой модуль и для практических задач было бы удобно иметь простую
# функцию в несколько строк, форматирующую данные с помощью ASCII-графики. Реализуйте эту функцию.
# Проверьте результат на одном из примеров из репозитория tabulate

def lengths(table): # Самое длинное слово в каждой строке
    ans = []
    for c in range(len(table[0])):
        ans.append(len(max([row[c] for row in table], key=lambda x: len(x))))
    return ans


def fill_blanks(table, l):
    table = [[row[i].center(l[i]) for i in range(len(row))] for row in table]
    return table


def tabulate_grid(table): # формирование таблицы
    l = lengths(table)
    table = fill_blanks(table, l)
    line = '+'
    line += '+'.join(['─' * (i + 2) for i in l])
    line += '+'
    print(line)
    for row in table:
        print('│ ', end='')
        print(*row, sep=' │ ', end=' │\n')
        print(line)


t1 = [('Masha', 'Nika', 'Nikita', 'Alena'),
      ('Nana', 'Alex', 'Roma', 'Andrew'),
      ('Yan', 'Anna', 'Arina', 'Ann'),
      ('Bob', 'Steve', 'Klark', 'Alan')]

tabulate_grid(t1)
