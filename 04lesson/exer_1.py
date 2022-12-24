""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов
 (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""

import random


def write_txt(arg):
    with open('output.txt', 'w') as data:
        data.write(arg)


def create_foundation(degree = 2):
    res = [random.randint(0, 99) for i in range(degree +1)]
    return res


def create_equation(args):
    res = []
    for i in range(len(args)):
        if args[i] !=0 and i == 0:
          res.append( str(args[i])+'x^2'+' + ' )
        elif i == 1 and args[i] != 0:
          res.append( str(args[i])+'x + ' )
        elif i == 2 and args[i] != 0:
            res.append(str(args[i])+ ' = 0')
    return ''.join(res)

write_txt(create_equation(create_foundation()))