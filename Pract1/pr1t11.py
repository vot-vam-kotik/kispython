'''Реализуйте синтезатор программ fast_mul_gen(y) для примеров из задачи 4.
 Воспользуйтесь ранее полученным кодом fast_mul. Ваша функция должна выдать текст функции f(x)
 (умножение на ранее заданный y), тело которой состоит из некоторого числа присваиваний.
  Для вывода функции используйте print. Добавьте автоматическое тестирование. Объясните,
   почему в общем случае у вас получается большее количество сложений, чем в примерах из задачи 4.'''


def fast_mul_gen(y):
    res = "def f(" + str(y) + "):\n\tx=" + str(y) + "\n"
    for i in range(0,y):
        res+="\tx += x \n"
    res+="\treturn x"
    return res

print(fast_mul_gen(5))