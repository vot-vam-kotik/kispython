'''Реализуйте функцию parse_subj(text) для разбора темы сообщения, поступающего к почтовому роботу.
Должны быть разобраны: группа (одна буква, например, «К» для «ИКБО») и номер варианта. Ниже показаны примеры
(в количестве 41) присланных тем, которые робот не сумел разобрать. Сможете ли вы
реализовать более интеллектуальный разбор?'''

def parse_group():
    bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py',
                'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12',
                'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21',
                'к2 в3', 'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10',
                'ПитонН4 н11', 'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']
    group = 'f';
    is_group = False
    j = 0
    for i in range(len(bad_subj)):
        for j in range (len(bad_subj[i])): # Проверка на группу
            if bad_subj[i][j].isdigit():
                if group != 'f': is_group = True
                break
            if bad_subj[i][j] == 'N' or bad_subj[i][j] == 'n' or bad_subj[i][j] == 'Н' or bad_subj[i][j] == 'н':
                if j == 5:
                    if bad_subj[i][0] == "P" or bad_subj[i][0] == "p" or bad_subj[i][0] == "П" or bad_subj[i][0] == "п":
                        continue
                group = 'ИНБО'
            if bad_subj[i][j] == 'V' or bad_subj[i][j] == 'v' or bad_subj[i][j] == 'В' or bad_subj[i][j] == 'в':
                group = 'ИВБО'
            if bad_subj[i][j] == 'K' or bad_subj[i][j] == 'k' or bad_subj[i][j] == 'К' or bad_subj[i][j] == 'к':
                group = 'ИКБО'
            if bad_subj[i][j] == 'N' and bad_subj[i][j] == "n" and bad_subj[i][j] == "Н" and bad_subj[i][j] == "н":
                group = 'ИНБО'
        if is_group:
            print(group, end = "") # Вывод наименования группы на экран
        group = 'f'
        if j + 1 != len(bad_subj[i]) and is_group: # Обнаружение номера группы
            while bad_subj[i][j].isdigit() == False and j + 1 != len(bad_subj[i]):
                j += 1
            if bad_subj[i][j].isdigit():
                print('-',bad_subj[i][j], end = "")
                j += 1
            if bad_subj[i][j].isdigit():
                print(bad_subj[i][j], end = "")
                j += 1
            print('-20', end = "")
        elif is_group and j+ 1== len(bad_subj[i]) and bad_subj[i][j].isdigit():
            print('-',bad_subj[i][j], '-20', end = "")
        if is_group: # Обнаружение варианта выполненного задания
            if j+1 >= len(bad_subj[i]):
                print(' Без варианта')
            elif j + 1 != len(bad_subj[i]):
                while bad_subj[i][j].isdigit() == False and j + 1 != len(bad_subj[i]):
                    j += 1
                if bad_subj[i][j].isdigit() == False and bad_subj[i][j+1].isdigit() == False:
                    print(' Без варианта', end = "")
                elif bad_subj[i][j].isdigit():
                    print(' Вариант:',bad_subj[i][j], end = "")
                    j += 1
                if j != len(bad_subj[i]):
                    if bad_subj[i][j].isdigit():
                        print(bad_subj[i][j], end = "")
                print('')
            elif is_group and j== len(bad_subj[i]) and bad_subj[i][j].isdigit():
                print(' Вариант:',bad_subj[i][j], '')
        is_group = False


parse_group()