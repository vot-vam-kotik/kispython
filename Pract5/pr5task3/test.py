'''Получите статистику по покрытию операторов.
Получите статистику по покрытию ветвей.
Постарайтесь изменить код исходной программы так, чтобы затруднить получение 100% покрытия.
Реализуйте вывод статистики о покрытии в HTML-представлении.'''


def incr(x):
    if (x != 10):
        x += 1
    elif x==5: # Постарайтесь изменить код исходной программы так, чтобы затруднить получение 100% покрытия.
        x += 2
    return x


def test_incr():
    assert incr(0) == 1
    assert incr(10) == 10

# cd C:/main/Study/Python/kispython/Pract5/pr5task3
# coverage run -m pytest test.py - Получите статистику по покрытию операторов
# coverage report
# coverage run --branch -m pytest test.py  Получите статистику по покрытию ветвей.
# coverage html Реализуйте вывод статистики о покрытии в HTML-представлении.