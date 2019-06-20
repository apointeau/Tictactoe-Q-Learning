# coding: utf-8

from tkinter import Canvas

TILE_SIZE  = 100
TILE_SPACE = 10


def board_left_click(event, play_callback):
    """
    This function is called at each left click on the board.
    It finds if there is a tile under the mouse position,
    and which one it is.
    """
    in_x = event.x % (TILE_SIZE + TILE_SPACE) <= TILE_SIZE
    in_y = event.y % (TILE_SIZE + TILE_SPACE) <= TILE_SIZE
    if in_x and in_y:
        idx_x = event.x // (TILE_SIZE + TILE_SPACE)
        idx_y = event.y // (TILE_SIZE + TILE_SPACE)
        play_callback(idx_x, idx_y)


def board_create(win, play_callback):
    """
    This function create a Tic Tac Toe graphical board.
    It binds a callback with the mouse left click, to catch actions.
    Board size is defined by the TILE_SIZE and TILE_SPACE. 
    """
    bsize = 3 * TILE_SIZE + 2 * TILE_SPACE
    board = Canvas(win,
        height=bsize, width=bsize,
        borderwidth=0, highlightthickness=0)
    board.create_rectangle(
        0, 0, bsize, bsize,
        fill="#60a3bc", outline="")
    for i in range(3*3):
        x = i % 3
        y = i // 3
        posx = x * TILE_SIZE + x * TILE_SPACE
        posy = y * TILE_SIZE + y * TILE_SPACE
        board.create_rectangle(
            posx, posy, posx + TILE_SIZE, posy + TILE_SIZE,
            fill="#82ccdd", outline="")
    board.bind("<Button-1>", lambda e: board_left_click(e, play_callback))
    board.pack()
    return(board)


def board_play(board, x, y, side):
    posx = x * TILE_SIZE + x * TILE_SPACE + 1/2 * TILE_SIZE
    posy = y * TILE_SIZE + y * TILE_SPACE + 1/2 * TILE_SIZE
    board.create_text(posx, posy,
        text=side, font=("Purisa", 60), fill="#3c6382")