# coding: utf-8

import sys
import os

from tkinter import Tk

from board import board_create, board_play


def is_winner(s):
    for i in range(3):
        if s[i][0] != 0 and s[i][0] == s[i][1] and s[i][1] == s[i][2]:
            return(s[i][0])
        if s[0][i] != 0 and s[0][i] == s[1][i] and s[1][i] == s[2][i]:
            return(s[0][i])
    if s[0][0] != 0 and s[0][0] == s[1][1] and s[1][1] == s[2][2]:
        return(s[1][1])
    if s[2][0] != 0 and s[2][0] == s[1][1] and s[1][1] == s[0][2]:
        return(s[1][1])
    return(0)


board = 0
side = 'X'
state = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
def play(x, y):
    global side, state
    if state[x][y] == 0:
        state[x][y] = 1 if side == 'X' else -1
        board_play(board, x, y, side)
        res = is_winner(state)
        if res != 0:
            winner = 'X' if res == 1 else 'O'
            print("Player {} win the game !".format(winner))
        side = 'O' if side == 'X' else 'X'

def main():
    global board
    win = Tk()
    win.title("Q-learning - Tic Tac Toe")
    board = board_create(win, play)
    win.mainloop()


if __name__ == "__main__":
    main()