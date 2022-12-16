#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
def sum (args):
    tmp = str(args).replace(' ','').replace('.','').replace(',','')
    result = 0
    some_list = list(tmp)
    for i in some_list:
        if (i != '(' and i != ')'):
          result += int(i)
    print(result)

a = 6782,2
b = 0.56

intro_list = [6782, 0.56, 737.11]
for i in intro_list:
    sum(i)

sum(b)


