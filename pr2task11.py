def barrose_willer():
    from itertools import groupby  # Для удобства вывода

    def rle_encode(info):  # Вспомогательная функция для вывода результата на экран
        return [(k, len(list(g))) for k, g in groupby(info)]

    def pr_preobr(str):  # Прямое преобразование
        str += '|'  # Добавляем разделитель, чтобы отслеживать перестановки
        # Создание "таблицы", которая содержит всё перестановки
        # Используем срезы :, чтобы помещать каждый символ в нужную ячейку
        permutations = [str[index:] + str[:index] for index, _ in enumerate(str)]
        # _ - это пропуск передачи значения. в данном случае счётчик будет начинать с 0
        permutations.sort()  # Сортировка по алфавиту
        new_str = [y[-1] for y in permutations]  # Прохождение по последнему столбцу "таблицы"
        new_str = ''.join(new_str)  # Запись последней буквы каждого столбца в новую строку
        return new_str  # Возврат результата

    def obr_preobr(str):  # Обратное преобразование
        table = list('')
        # Создание списка, который содержит в себе прямое преобразование в качестве "столбца" для таблицы
        for i in range(len(str)):
            table.append(str[i])
        for i in range(len(str) - 1):  # Пока "столбец" не пройден до конца выполняется цикл
            table.sort()  # Текущий "столбец" сортируем по алфавиту
            table = [str[i] + table[i] for i in range(len(str))]  # Добавляем идентичный входному "столбцу" "столбец"
        return table[
            [x[-1] for x in table].index('|')]  # Вернем ту строку, в исходной которой в конце стоял разделитель

    st_r = 'AMAMAMAMAMLALALALALMAMLAM'  # Входная строка
    print('Строка:', st_r)
    result1 = pr_preobr(st_r)
    for_2 = result1
    result1 = result1.replace('|',
                              '')  # Возвращение копии строки, в которой все вхождения подстроки # заменяются новой подстрокой (пустой)
    print('Результат прямого преобразования', result1)
    result2 = obr_preobr(for_2)
    print('Результат обратного преобразования', result2.replace('|',
                                                                ''))  # Возвращение копии строки, в которой все вхождения подстроки # заменяются новой подстрокой (пустой)
    print('Обычное RLE-сжатие', rle_encode(st_r))
    print('RLE сжатие с пользованием преобразования Барроуза-Уилера', rle_encode(result1))


barrose_willer()