"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc
"""

f = open('income_1.txt', 'r')
k = open('output_exr.txt', 'r')


def write_txt(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('output_exr.txt', 'w') as data:
          data.write(res)
    return wrapper
@  write_txt
def coding(arg):
    count = 1
    res = ''
    for i in range(len(arg)-1):
        if arg[i] == arg[i+1]:
            count += 1
        else:
            res = res + str(count) + arg[i]
            count = 1
    if count > 1 or (arg[len(arg)-2] != arg[-1]):
        res = res + str(count) + arg[-1]
    return res


def decoding(arg):
    number = ''
    res = ''
    for i in range(len(arg)):
        if not arg[i].isalpha():
            number += arg[i]
        else:
            res = res + arg[i] * int(number)
            number = ''
    print (f"{arg} -> {res}")
    return res



from_input_file = f.read()
coding(from_input_file)
decoding(k.read())
