def lengths(table):
    ans = []
    for c in range(len(table[0])):
        ans.append(len(max([row[c] for row in table], key=lambda x: len(x))))
    return ans


def fill_blanks(table, l):
    table = [[row[i].center(l[i]) for i in range(len(row))] for row in table]
    return table


def tabulate(table):
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


t1 = [('Alexa', 'Nana', 'Nana', 'Anna'),
      ('Nana', 'Alexa', 'Anna', 'Nana'),
      ('Nana', 'Anna', 'Alexa', 'Nana'),
      ('Anna', 'Nana', 'Sasha', 'Alexa')]

tabulate(t1)
