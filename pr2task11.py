# Преобразование Барроуза-Уиллера
def burrows_wheeler():
    from itertools import groupby  # для удобства вывода

    def rle_encode(info):  # вспомогательная функция для вывода результата на экран
        return [(k, len(list(g))) for k, g in groupby(info)]

    def pr_preobr(str):  # прямое преобразование
        str += '|'  # добавляем разделитель, чтобы отслеживать перестановки
        # создание "таблицы", которая содержит всё перестановки
        # используем срезы :, чтобы помещать каждый символ в нужную ячейку
        permutations = [str[index:] + str[:index] for index, _ in enumerate(str)]
        # _ - это пропуск передачи значения. в данном случае счётчик будет начинать с 0
        permutations.sort()  # сортировка по алфавиту
        new_str = [y[-1] for y in permutations]  # прохождение по последнему столбцу "таблицы"
        new_str = ''.join(new_str)  # запись последней буквы каждого столбца в новую строку
        return new_str  # возврат результата

    def obr_preobr(str):  # обратное преобразование
        table = list('')
        # создание списка, который содержит в себе прямое преобразование в качестве "столбца" для таблицы
        for i in range(len(str)):
            table.append(str[i])
        for i in range(len(str) - 1):  # пока "столбец" не пройден до конца выполняется цикл
            table.sort()  # текущий "столбец" сортируем по алфавиту
            table = [str[i] + table[i] for i in range(len(str))]  # добавляем идентичный входному "столбцу" "столбец"
        return table[
            [x[-1] for x in table].index('|')]  # вернем ту строку, в исходной которой в конце стоял разделитель

    st_r = 'AMAMAMAMAMLALALALALMAMLAM'  # входная строка
    print('Строка:', st_r)
    result1 = pr_preobr(st_r)
    for_2 = result1
    result1 = result1.replace('|',
                              '')  # возвращение копии строки, в которой все вхождения подстроки # заменяются новой подстрокой (пустой)
    print('Результат прямого преобразования', result1)
    result2 = obr_preobr(for_2)
    print('Результат обратного преобразования', result2.replace('|',
                                                                ''))  # возвращение копии строки, в которой все вхождения подстроки # заменяются новой подстрокой (пустой)
    print('Обычное RLE-сжатие', rle_encode(st_r))
    print('RLE сжатие с пользованием преобразования Барроуза-Уилера', rle_encode(result1))


burrows_wheeler()