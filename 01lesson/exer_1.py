# This is a sample Python script.

# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

def check_day(args):
    if 1 <= args <= 5:
        print('False')
    elif 6 <= args <= 7:
        print('True')


monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 7

check_day(saturday)
check_day(sunday)
check_day(monday)
