"""Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10"""

income_lst = [45,3,2,10]
def convert (arg):
   n=''

   while arg > 0:
       y = str(arg % 2)
       n = y + n
       arg = int(arg / 2)
   print(n)

for i in income_lst:
    convert(i)