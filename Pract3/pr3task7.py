import random as r
from secrets import token_hex

from numpy import linspace
from numpy import vstack

from matplotlib import pyplot as plt
from matplotlib import colors

# палитра цветов для спрайтов
COLORMAP = plt.cm.magma

# количество спрайтов в строке/столбце
# минимальное значение - 2
SPRITE_N = 5

# количество матриц спрайтов для генерации
IMAGE_NUM = 1

# оттенки цветовой карты
RANGE = 0.,1.


# добавление белого цвета в цвет.карту
def add_white(colormap):
    white = plt.cm.binary(0)
    colormap = colormap(linspace(0, 1, 255))  # 255 так как 1 занято белым
    colormap = vstack((white, colormap))

    # каст в колормап для матплотлиба
    return colors.LinearSegmentedColormap.from_list('my_colormap', colormap)


# значение для каждого пикселя
def pixel():
    if r.choice([0, 1, 2]) == 0:
        return 0
    else:
        return r.uniform(max(RANGE[0], 1/256), RANGE[1])


# создание самих спрайтов
def make_mx():
    mx = [[pixel() for _ in range(3)] for _ in range(5)]
    for i in mx:
        i += i[-2::-1]
    return mx

# конвертация матрицы в видимое изображение
def build_sprites():
    colormap = add_white(COLORMAP)
    for _ in range(IMAGE_NUM):
        pic_name = f'gen_sprites_{COLORMAP.name}_{SPRITE_N:>02}_{token_hex(4)}'
        fig, axs = plt.subplots(SPRITE_N, SPRITE_N)
        for i in axs:
            for j in i:
                j.imshow(make_mx(), cmap=colormap)
                j.axis('off')

        plt.subplots_adjust(wspace=0.4, hspace=0.4)
        plt.savefig(pic_name, bbox_inches='tight')
        plt.close()


build_sprites()
