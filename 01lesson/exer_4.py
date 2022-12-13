#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def ret_parts (args):
    if args <= 0:
        print('input is out for positive value, \nplease restart and try again')
    elif args == 1:
        print(f'you input part: {args} '
              f'\nand values of part in range from axis X = 1 to infinity and axis Y = 1 to infinity')
    elif args == 2:
        print(f'you input part: {args} '
              f'\nand values of part in range from axis Y = 1 to infinity and axis X = -1 to minus infinity')
    elif args == 3:
        print(f'you input part: {args} '
              f'\nand values of part in range from axis X = -1 to minus infinity and axis Y = -1 to minus infinity')
    elif args == 4:
        print(f'you input part: {args} '
              f'\nand values of part in range from axis X = 1 to infinity and axis Y = -1 to minus infinity')
number = 0
user_input = int(input('input a number of parts in range 1 to 4: '))

if 1 <= user_input <= 4:
    number = user_input
else:
    print('number is out if range')
    user_input = int(input('input a number of parts in range 1 to 4: '))
    while 4 <= user_input:
      user_input = int(input('input a number of parts in range 1 to 4: '))
    number = user_input

ret_parts(number)