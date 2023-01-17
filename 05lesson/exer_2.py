"""
Создайте программу для игры в 'Крестики-нолики'
НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
"""

import random
from tkinter import *

window = Tk()
window.title('Some-Game')

game_run = True
field = []
cross_count = 0
zero = 'O'

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'aqua'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')


def check_win(zero):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], zero)
        check_line(field[0][n], field[1][n], field[2][n], zero)
    check_line(field[0][0], field[1][1], field[2][2], zero)
    check_line(field[2][0], field[1][1], field[0][2], zero)


def check_line(a1, a2, a3, zero):
    if a1['text'] == zero and a2['text'] == zero and a3['text'] == zero:
        a1['background'] = a2['background'] = a3['background'] = 'crimson'
        global game_run
        game_run = False


def can_win(a1, a2, a3, zero):
    result = False
    if a1['text'] == zero and a2['text'] == zero and a3['text'] == ' ':
        a3['text'] = 'O'
        result = True
    if a1['text'] == zero and a2['text'] == ' ' and a3['text'] == zero:
        a2['text'] = 'O'
        result = True
    if a1['text'] == ' ' and a2['text'] == zero and a3['text'] == zero:
        a1['text'] = 'O'
        result = True
    return result


def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], zero):
            return
        if can_win(field[0][n], field[1][n], field[2][n], zero):
            return
    if can_win(field[0][0], field[1][1], field[2][2], zero):
        return
    if can_win(field[2][0], field[1][1], field[0][2], zero):
        return

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = zero
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(text=' ', width=6, height=3,
                        font=('Verdana', 22, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(text='New_Game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

window.mainloop()