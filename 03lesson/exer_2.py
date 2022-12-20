"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]"""


first_lst = [2, 3, 4, 5, 6]
second_lst = [2, 3, 5, 6]
result =[]

def multy_idx (arg):
    for i in arg:
        a = arg.pop(len(arg) - 1)
        b = arg.pop(0)
        result.append(a*b)
        if len(arg) == 1:
            result.append(arg.pop(0)** 2)


multy_idx(first_lst)
print (result)
result.clear()
multy_idx(second_lst)
print (result)
