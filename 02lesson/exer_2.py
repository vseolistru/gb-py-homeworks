# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = 4
list_res = []

def sum (args):
    result = 0
    for i in args:
          result += i
    print(result)


for i in range(1, n+1):
    list_res.append(round((1+1/i)**i, 3))

sum(list_res)