from pathlib import Path
import tkinter as tk

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]


def draw_line(coords, color_index):
    if len(coords) <= 1:
        return
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


def draw_corner(args, color, isY=True):     # Отрисовка команды 0xF4 (Ось Y) и 0xF5 (Ось Х)
    x, y = args[:2]
    coords = [(x, y)]
    for arg in args[2:]:
        x, y = (x, arg) if isY else (arg, y)
        isY = not isY
        coords.append((x, y))
    draw_line(coords, color)


def draw_abs(args, color):     # Команда  0xF6 (абсолютная линия)
    coords = [tuple(args[:2])]
    for arg1, arg2 in zip(args[2::2], args[3::2]):
        coords.append((arg1, arg2))
    draw_line(coords, color)


def draw_rel(args, color): # команда 0xF7 (относительная линия)
    x, y = args[:2]
    coords = [(x, y)]
    for arg in args[2:]:
        xd, yd = arg >> 4 & 7, arg & 7
        xs, ys = arg >> 4 & 8, arg & 8
        x += -xd if xs else xd
        y += -yd if ys else yd
        coords.append((x, y))
    draw_line(coords, color)


def draw(pic):     # парсер команд из файла
    commands = []
    index = -1
    for byte in pic:
        if byte >= 0xf0:
            commands.append([])
            index += 1
        commands[index].append(byte)

    # переменные экрана
    piccolor = picdraw = None

    # выполнение команд отрисовки
    for cmd in commands:
        action, *args = cmd
        if action == 0xf0:
            picdraw = True
            piccolor = args[0]
            continue
        if action == 0xf1:
            picdraw = False
            continue
        if action == 0xf4 and picdraw:
            draw_corner(args, piccolor, isY=True)
            continue
        if action == 0xf5 and picdraw:
            draw_corner(args, piccolor, isY=False)
            continue
        if action == 0xf6 and picdraw:
            draw_abs(args, piccolor)
            continue
        if action == 0xf7 and picdraw:
            draw_rel(args, piccolor)
            continue


pic = Path('PIC.28').read_bytes()
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()