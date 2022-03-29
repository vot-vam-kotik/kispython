#Как вы думаете, модуль загружается один раз или загружается каждый раз при очередном импорте?
# Докажите правильность вашей гипотезы кодом
import module_1

module_1.print_hello()

import os

# меняем местами файлы
os.rename("module_1.py", "module_3.py")
os.rename("module_2.py", "module_1.py")
os.rename("module_3.py", "module_2.py")

import module_1
module_1.print_hello()

