'''Добавьте к программе контракты pre, post, ensure, raises, reason.
Найдите программу, для которой контракт has будет полезен.
Для программы с классами используйте инвариант inv.
Для тестирования контрактов используйте pytest.'''
import pytest
import deal


@deal.pre(lambda q, p: q >= 0 and p >= 0)
@deal.post(lambda result: result[0] >= 0 and result[1] >= 0)
@deal.ensure(lambda q, p, result: result == (q // p, q % p))
@deal.reason(ZeroDivisionError, lambda q, p: p == 0)
@deal.raises(ZeroDivisionError)
@deal.has()
def divrem(q, p):
    '''
    Функция divrem возвращает частное и остаток от деления.
    '''
    d = 0
    if p == 0:
        raise ZeroDivisionError
    while q >= p:
        q -= p
        d += 1
    return d, q


def test_divrem():
    divrem(10, 5)
    with pytest.raises(ZeroDivisionError):
        divrem(0, 0)
    divrem(0, 1)