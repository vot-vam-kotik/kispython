def delete_duplicate_columns(table):
    for row in table:
        row[2] = ""
    return table


def delete_duplicate_rows(table):
    dup_free = []
    dup_free_set = set()
    for x in table:
        if tuple(x) not in dup_free_set:
            dup_free.append(x)
            dup_free_set.add(tuple(x))
    table = dup_free
    return dup_free


def transformer(i, value):
    if i == 0:
        date = value.split("-")
        return f'{date[2]}.{date[1]}.{date[0]}'

    if i == 1:
        name = value.split(",")
        return f'{name[0]}'
    if i == 2:
        value = value[2:]
        value = f'{value[:3]} {value[3:]}'
        value = f'{value[:7]}-{value[7:]}'
        return value
    if i == 3:
        return "Y" if value == "Выполнено" else "N"


def separate_column(table):
    for i in range(len(table)):
        temp = table[i][3].split("&")
        table[i][2] = temp[0]
        table[i][3] = temp[1]
    return table


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(j, table[i][j])
    return table


def main(table):
    return transform(
        separate_column(
            delete_duplicate_rows(
                delete_duplicate_columns(table))
        )
    )



table = [
    ['02-11-14', 'Салин, Л.К', 'Салин, Л.К.', '+71468045864&Не выполнено'],
    ['03-06-25', 'Чирман, А.В.', 'Чирман, А.В.', '+71467578085&Не выполнено'],
    ['01-03-27', 'Наков, Д.К.', 'Наков, Д.К.', '+72913292261&Выполнено'],
    ['01-03-27', 'Наков, Д.К.', 'Наков, Д.К.', '+72913292261&Выполнено']
]

print(transform(separate_column(delete_duplicate_rows(delete_duplicate_columns(table)))))
