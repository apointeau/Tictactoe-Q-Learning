# coding: utf-8

import random

from tkinter import Tk, Canvas


TILE_SIZE  = 100
TILE_SPACE = 10

class Morpion():

    def __init__(self, display=True):
        self.display = display
        if self.display:
            # Create graphical windows
            self.win = Tk()
            self.win.title("Q-learning - Tic Tac Toe")
            # Create main canvas
            self.canvas_size = 3 * TILE_SIZE + 2 * TILE_SPACE
            self.canvas = Canvas(self.win,
                height=self.canvas_size, width=self.canvas_size,
                borderwidth=0, highlightthickness=0)

    def _event_button1(self, event):
        if self.players[self.players_turn] == "human":
            in_x = event.x % (TILE_SIZE + TILE_SPACE) <= TILE_SIZE
            in_y = event.y % (TILE_SIZE + TILE_SPACE) <= TILE_SIZE
            if in_x and in_y:
                idx_x = event.x // (TILE_SIZE + TILE_SPACE)
                idx_y = event.y // (TILE_SIZE + TILE_SPACE)
                self.play(idx_x, idx_y)

    def _event_key(self, event):
        if event.char in ['r', 'R']:
            print("Restart ...")
            self.start(self.players[0], self.players[1])

    def _reset_graphical_coponents(self):
        self.canvas.delete("all")
        # Create background
        self.canvas.create_rectangle(
            0, 0, self.canvas_size, self.canvas_size,
            fill="#60a3bc", outline="")
        for i in range(3*3):
            x = i % 3
            y = i // 3
            posx = x * TILE_SIZE + x * TILE_SPACE
            posy = y * TILE_SIZE + y * TILE_SPACE
            # Create tile
            self.canvas.create_rectangle(
                posx, posy, posx + TILE_SIZE, posy + TILE_SIZE,
                fill="#82ccdd", outline="")
        self.canvas.bind("<Button-1>", self._event_button1)
        self.canvas.pack()
        self.win.bind_all('<Key>', self._event_key)


    def start(self, player1="human", player2="human"):
        if self.display:
            self._reset_graphical_coponents()
        self.map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.players = [player1, player2]
        self.players_turn = random.randint(0, 1)
        self.players_symbols = ['X', 'O']
        print("Player{} starts with the symbol '{}' ...".format(
            self.players_turn + 1, self.players_symbols[self.players_turn]))
        self.win.mainloop()

    def _play_graphical(self, x, y, symbol):
        posx = x * TILE_SIZE + x * TILE_SPACE + 1/2 * TILE_SIZE
        posy = y * TILE_SIZE + y * TILE_SPACE + 1/2 * TILE_SIZE
        self.canvas.create_text(posx, posy,
            text=symbol, font=("Purisa", 60), fill="#3c6382")

    def play(self, x, y):
        if self.players_turn != -1 and self.map[x][y] == 0:
            self.map[x][y] = self.players_turn + 1
            symbol = self.players_symbols[self.players_turn]
            self._play_graphical(x, y, symbol)

            winner = self.is_winner()
            if winner == -1:
                self.players_turn = -1
                print("It's a draw, no winner, <press R to restart>")
            elif winner > 0:
                self.players_turn = -1
                print("Player{} win the game !, <press R to restart>".format(winner))
            else:
                self.players_turn = 1 if self.players_turn == 0 else 0


    def is_winner(self):
        m = self.map
        for i in range(3):
            if m[i][0] != 0 and m[i][0] == m[i][1] and m[i][1] == m[i][2]:
                return(m[i][0])
            if m[0][i] != 0 and m[0][i] == m[1][i] and m[1][i] == m[2][i]:
                return(m[0][i])
        if m[0][0] != 0 and m[0][0] == m[1][1] and m[1][1] == m[2][2]:
            return(m[1][1])
        if m[2][0] != 0 and m[2][0] == m[1][1] and m[1][1] == m[0][2]:
            return(m[1][1])
        if set(m[0] + m[1] + m[2]) == set([1, 2]): # map full == no winner, game end
            return (-1)
        return(0)

def main():
    game = Morpion()
    game.start("human", "human")

if __name__ == "__main__":
    main()