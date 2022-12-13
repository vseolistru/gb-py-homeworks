""" Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """
import random

'AB = √(xb - xa)2 + (yb - ya)2'
'((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)'


first_point = []
second_point = []


def get_distance(args, args1):
    return (((args1[0] - args[0]) ** 2 + (args1[1] - args[1]) ** 2) ** (0.5))


for i in range(2):
    first_point.append(random.randint(0, 10))
    second_point.append(random.randint(0, 10))

print (f'{first_point}, {second_point} result-> {get_distance(first_point, second_point)}')


