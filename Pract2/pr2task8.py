'''Реализуйте генератор случайных данных ФИО.
Список распространенных имен позволяется скачать
из интернета. Фамилии необходимо генерировать самостоятельно.
Впрочем, можете попробовать генерировать и имена.'''

import random

names = ['Мария', 'Анна', 'Виктория', 'Анастасия', 'Алиса', 'Полина', 'Елизавета', 'Александра', 'Дарья', 'Варвара',
         'Екатерина', 'София', 'Ксения', 'Арина', 'Василиса', 'Вероника', 'Ева', 'Валерия', 'Милана', 'Ульяна', 'Кира']
ignore = ['Ю', 'Ь', 'Ъ', 'Й', 'Ё', 'Ы']
at = [chr(x) for x in range(ord('А'), ord('Я') + 1) if chr(x) not in ignore]
random_end = ['ова', 'ева', 'ина', 'ын', 'ская', 'цкая', 'ская', 'як', 'ая', 'енкова', 'их', 'ых', 'ко']
vowel = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'e']
consonant = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

def generate_random_fio():
    s = random.choice(names) + " " + random.choice(at) + ". "
    for i in range(random.randint(1, 3)):
        if i == 0:
            s += random.choice(consonant).upper()
        else:
            s += random.choice(consonant)
        s += random.choice(vowel)
    s = s + random.choice(consonant) + random.choice(random_end)
    return s

print(generate_random_fio())