from kandinsky import *
from ion import *
import time

# screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = (320, 222)

GAME_WIDTH = 216
CASE_WIDTH = GAME_WIDTH // 8

HORIZONTAL_BORDER = (SCREEN_WIDTH - GAME_WIDTH) // 2
VERTICAL_BORDER = (SCREEN_HEIGHT - GAME_WIDTH) // 2

# colors
colors = {
    "brown": (240, 217, 181),
    "beige": (181, 136, 99),
    "black": (0, 0, 0),
    "lblack": (60, 60, 60),
    "white": (255, 255, 255),
    "lwhite": (243, 243, 243),
    "green": (100, 109, 64) 
}

whites = ["K", "N", "B", "P", "Q", "R"]

# game resources
res = {
    "k":[
        ['', '', '', '', '', 'b', 'b', '', '', '', '', ''],
        ['', '', '', '', 'b', 'c', 'c', 'b', '', '', '', ''],
        ['', '', '', '', 'b', 'c', 'c', 'b', '', '', '', ''],
        ['', 'b', 'b', 'b', '', 'b', 'b', '', 'b', 'b', 'b', ''],
        ['b', 'c', 'c', 'c', 'b', '', '', 'b', 'c', 'c', 'c', 'b'],
        ['b', 'c', '', 'b', 'c', 'b', 'b', 'c', 'b', '', 'c', 'b'],
        ['b', 'c', '', '', 'b', 'c', 'c', 'b', '', '', 'c', 'b'],
        ['b', 'c', 'b', '', '', 'c', 'c', '', '', 'b', 'c', 'b'],
        ['', 'b', 'c', 'b', 'b', 'c', 'c', 'b', 'b', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '']
        ],
    "q":[
        ['', '', '', '', '', '', 'b', 'b', '', '', '', '', '', ''],
        ['', '', '', '', '', 'b', 'c', 'c', 'b', '', '', '', '', ''],
        ['', '', '', '', '', 'b', 'c', 'c', 'b', '', '', '', '', ''],
        ['', '', '', '', '', '', 'b', 'b', '', '', '', '', '', ''],
        ['b', '', '', '', '', '', '', '', '', '', '', '', '', 'b'],
        ['', 'b', 'b', '', '', '', 'b', 'b', '', '', '', 'b', 'b', ''],
        ['', 'b', 'c', 'b', '', 'b', 'c', 'c', 'b', '', 'b', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'b', 'c', 'c', 'c', 'c', 'b', 'c', 'c', 'b', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', '', ''],
        ['', '', '', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '', '', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '', '']
        ],
    "b":[
        ['', '', '', '', 'b', 'b', '', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'b', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'b', '', '', ''],
        ['', '', '', '', 'b', 'b', '', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'b', '', '', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'b', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', ''],
        ['b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b'],
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        ],
    "n":[
        ['', '', 'b', 'b', 'b', 'b', '', '', '', '', '', ''],
        ['', '', 'b', 'c', 'c', 'c', 'b', 'b', 'b', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', 'b', 'c', 'b', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['b', 'c', 'c', 'c', 'c', 'c', 'b', 'c', 'c', 'c', 'b', ''],
        ['b', 'c', 'c', 'b', 'c', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'b', '', '', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', '', '', '', 'b', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', '', '', 'b', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '']
        ],
    "r":[
        ['', 'b', 'b', 'b', '', 'b', 'b', 'b', 'b', 'b', 'b', ''],
        ['', 'b', 'c', 'b', '', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', '', '', 'b', 'b', 'b', 'b', 'b', 'b', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'c', 'c', 'b', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'c', 'c', 'b', '', '', ''],
        ['', '', '', 'b', 'c', 'c', 'c', 'c', 'b', '', '', ''],
        ['', '', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', ''],
        ['b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b'],
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        ],
    "p":[
        ['', '', 'b', 'b', 'b', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', '', 'b', 'c', 'c', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['', '', 'b', 'c', 'c', 'b', '', ''],
        ['', 'b', 'c', 'c', 'c', 'c', 'b', ''],
        ['b', 'c', 'c', 'c', 'c', 'c', 'c', 'b'],
        ['b', 'c', 'c', 'c', 'c', 'c', 'c', 'b'],
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        ]
}

# position
position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
board = []

view = "white"

# functions

def fill_case(x, y, color):
    if view == "black":
        x = 7 - x
        y = 7 - y
    fill_rect(HORIZONTAL_BORDER + CASE_WIDTH * x, VERTICAL_BORDER + CASE_WIDTH * y, CASE_WIDTH, CASE_WIDTH, colors[color])

def get_piece_color(piece):
    return "white" if piece in whites else "black"

def get_case_color(x, y):
    return "brown" if (x + y) % 2 == 0 else "beige"

def draw_piece(x, y, piece):
    if view == "black":
        x = 7 - x
        y = 7 - y
    piece_res = res[piece.lower()]

    border_x = (CASE_WIDTH - len(piece_res[0])) // 2
    border_y = (CASE_WIDTH - len(piece_res)) // 2

    place_y = 1

    color = colors["l" + get_piece_color(piece)]

    for row in piece_res:
        place_x = 0
        for pixel in row:
            if pixel:
                fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH + border_x + place_x, VERTICAL_BORDER + y * CASE_WIDTH + border_y + place_y, 1, 1, color if pixel == "c" else colors["black"])
            place_x += 1
        place_y += 1
    
# CURSOR
cursor_width = 2

def draw_cursor(x, y):
    if view == "black":
        x = 7 - x
        y = 7 - y
    
    #left
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH, VERTICAL_BORDER + y * CASE_WIDTH, cursor_width, CASE_WIDTH, colors["green"])
    # top
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH, VERTICAL_BORDER + y * CASE_WIDTH, CASE_WIDTH, cursor_width, colors["green"])
    # right
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH + CASE_WIDTH - cursor_width, VERTICAL_BORDER + y * CASE_WIDTH, cursor_width, CASE_WIDTH, colors["green"])
    # bot
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH, VERTICAL_BORDER + y * CASE_WIDTH + CASE_WIDTH - cursor_width, CASE_WIDTH, cursor_width, colors["green"])

def erase_cursor(x, y):
    if view == "black":
        x = 7 - x
        y = 7 - y
    color = get_case_color(x, y)
    # left
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH, VERTICAL_BORDER + y * CASE_WIDTH, cursor_width, CASE_WIDTH, colors[color])
    # top
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH, VERTICAL_BORDER + y * CASE_WIDTH, CASE_WIDTH, cursor_width, colors[color])
    # right
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH + CASE_WIDTH - cursor_width, VERTICAL_BORDER + y * CASE_WIDTH, cursor_width, CASE_WIDTH, colors[color])
    # bot
    fill_rect(HORIZONTAL_BORDER + x * CASE_WIDTH, VERTICAL_BORDER + y * CASE_WIDTH + CASE_WIDTH - cursor_width, CASE_WIDTH, cursor_width, colors[color])

# SELECTION
def draw_select(x, y):
    # it's done before cause it's general whereas there are specific things that needs to be managed later
    fill_case(x, y, "green")
    if view == "black":
        x = 7 - x
        y = 7 - y
    filling = board[y][x]
    if filling:
        draw_piece(x, y, filling)

def erase_select(x, y):
    if view == "black":
        x = 7 - x
        y = 7 - y
    fill_case(x, y, get_case_color(x, y))
    filling = board[y][x]
    if filling:
        draw_piece( x, y, filling)

# load board from position ~ setting board
loaded = position.split("/")
board = [["" for _ in range(8)] for _ in range(8)]
y = 0
for i in range(8):
    x = 0
    for element in loaded[i]:
        if '0' <= element <= '9':
            x += int(element)
        else:
            board[y].insert(x, element)
        x += 1
    y += 1
del(loaded)
del(position)

# drawing board func
def draw_board():
    for y in range(8):
        for x in range(8):
            color = "brown" if (x + y) % 2 == 0 else "beige"
            fill_case(x, y, color)

    # draw pieces
    for y in range(8):
        for x in range(8):
            if board[y][x]:
                draw_piece(x, y, board[y][x])

while True:
    draw_board()
    time.sleep(5)
    view = "black" if view == "white" else "white"
