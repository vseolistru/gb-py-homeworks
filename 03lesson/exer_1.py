"""Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом."""



new_lst = [11,22,33,44,55,66]
some_lst = [2, 3, 5, 9, 3]


def some_count (arg):
    res = 0
    for i in range(len(arg)):
        if i % 2 == 1:
            res += arg[i]
    return res

res = some_count(new_lst)
print (res)

res = some_count(some_lst)
print (res)