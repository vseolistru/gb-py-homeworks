"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит заданное количество конфет.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
 Все конфеты оппонента достаются сделавшему последний ход.
a) Добавьте игру против бота
b) Подумайте как наделить бота 'интеллектом'
"""

from random import randint


from random import randint


def start_data(name):
    start_candies = int(
        input(f"{name},"
        f" input candies in range from 1 to 28: "
        ))
    while start_candies < 1 or start_candies > 28:
        start_candies = int(
            input(f"{name},"
            f" oop's, pls input correct quantity candies: "
        ))
    return start_candies


def steps_result_process(name, k, counter, value):
    print(
        f"Make step {name},"
        f" he took {k},"
        f" now, he have a {counter}."
        f" On a board last {value} candies."
    )


player1 = input("Input a first player name: ")
player2 = input("Input a second player name: ")
value_allof_candies = int(input("Input quantity all of candies for a game: "))
step = randint(0, 2)


if step:
    print(f"First step {player1}")
else:
    print(f"Second step {player2}")

first_player_counter = 0
second_player_counter = 0

while value_allof_candies > 28:
    if step:
        step_candies = start_data(player1)
        first_player_counter += step_candies
        value_allof_candies -= step_candies
        step = False
        steps_result_process(player1, step_candies, first_player_counter, value_allof_candies)
    else:
        next_step_candies = start_data(player2)
        second_player_counter += next_step_candies
        value_allof_candies -= next_step_candies
        step = True
        steps_result_process(player2, next_step_candies, second_player_counter, value_allof_candies)

if step:
    print(f"{player1} - Win this game")
else:
    print(f"{player2} - Win this game")