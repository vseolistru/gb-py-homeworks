"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи"""

n= 9
res=[]
result = []
def concat(args, kwargs, n):
    new_result = []
    for i in args:
        new_result.append(i)
    for i in kwargs:
        new_result.append(i)
    new_result.pop(n)
    return new_result

def fibonacci(n):
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_negative_reverse(new_reverse):
    for i in range(len(new_reverse)):
        if i % 2 == 0:
            tmp = str(new_reverse[i])
            res = '-' + tmp
            result.append(int(res))
        else:
            result.append(new_reverse[i])

for i in range(n+1):
    res.append(fibonacci(i))

new_reverse = res[::-1]
get_negative_reverse(new_reverse)

print(concat(result, res, n))