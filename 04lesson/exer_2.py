"""Даны два файла, в каждом из которых находится запись многочлена.
 Задача - сформировать файл, содержащий сумму многочленов."""


f = open('income_1.txt', 'r')
k = open('income_2.txt', 'r')


def write_txt(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('output_exr.txt', 'w') as data:
          data.write(res)
    return wrapper


def get_values (args1, args2):
    first_equation = 0
    second_equation = 0
    if args1[2] == 'x' or args1[1] == 'x':
      first_equation = ''.join(args1).replace('x','').replace('^2','').replace(' ','').replace('=0','').split('+',2)
    else:
        print('your data is not required equation')
    if args2[2] == 'x' or args2[1] == 'x':
      second_equation = ''.join(args2).replace('x','').replace('^2','').replace(' ','').replace('=0','').split('+',2)
    else:
        print('your data is not required equation')

    first_equation = [int(i) for i in first_equation]
    second_equation = [int(i) for i in second_equation]
    sum = list(map(lambda first_equation, second_equation: first_equation + second_equation, first_equation, second_equation))
    return sum


@write_txt
def create_equation(args):
    result = ''
    for i in range(len(args)):
        if i == 0:
          result += str(args[i])+'x^2 + '
        elif i == 1:
            result += str(args[i])+'x + '
        else:
            result += str(args[i])
    return result


create_equation(get_values(f.read(), k.read()))