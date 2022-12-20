"""Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
Пример:
[1.1, 1.2, 3.45, 5, 10.21] => 0.19"""
import re

arg = []
income_lst = [1.17, 1.2, 3.661, 5, 10.221]

def get_values(arg):
    crude_str = ' '.join(arg)
    res = []
    res_new_cleared_lst = re.findall('\.\w*', crude_str)
    for i in res_new_cleared_lst:
        tmp = ''.join(i).replace('.','')
        if len(tmp)== 1:
            order_tmp = tmp+'0'
            res.append(int(order_tmp))
        elif tmp[0] == '0':
            order_tmp =(tmp[1])
            res.append(int(order_tmp))
        else:
            order_tmp = tmp[0]+tmp[1]
            res.append(int(order_tmp))
    return res

def diff (args):
    diff = max(args) - min(args)
    resulst = '0.' + str(diff)
    return resulst

for i in income_lst:
    arg.append(str(i))

some_tmp_result = get_values(arg)
print(diff(some_tmp_result))
