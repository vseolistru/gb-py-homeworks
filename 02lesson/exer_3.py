"""Реализуйте алгоритм перемешивания списка.
 НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
 библиотеки Random для и получения случайного int"""
import random

def func_sort(arg):
    for i in range(len(arg)-1):
        if arg[i] > arg[i+1]:
           arg[i], arg[i+1] = arg[i+1], arg[i]
    print(arg)


value = random.randint(0, 10)
list_point = []

for i in range(value):
    list_point.append(random.randint(0, 10))

print(list_point)
func_sort(list_point)




