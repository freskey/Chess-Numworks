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
        place_x = 1
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

# MOVES
def find_moves(x, y):
    return []


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
    # drawing board
    for y in range(8):
        for x in range(8):
            color = "brown" if (x + y) % 2 == 0 else "beige"
            fill_case(x, y, color)

    # draw pieces
    for y in range(8):
        for x in range(8):
            if board[y][x]:
                draw_piece(x, y, board[y][x])

# setting generals variables
cursor = {
    "x":{
        "white":4,
        "black":4 
        },
    "y":{
        "white":6,
        "black":1
    }
}

select = {
    "x":None,
    "y":None
}
selected = False

moves = []

# GAME LOOP
while True:
    draw_board()
    draw_cursor(cursor['x'][view], cursor['y'][view])

    current_view = view

    while current_view == view:
        # movements
        if keydown(KEY_LEFT):
            if cursor['x'][view] != 0 if view == "white" else 7:
                if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                    erase_cursor(cursor['x'][view], cursor['y'][view])
                cursor['x'][view] += -1 if view == "white" else 1
            if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                draw_cursor(cursor['x'][view], cursor['y'][view])
        if keydown(KEY_RIGHT):
            if cursor['x'][view] != 7 if view == "white" else 0:
                if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                    erase_cursor(cursor['x'][view], cursor['y'][view])
                cursor['x'][view] += 1 if view == "white" else -1
                if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                    draw_cursor(cursor['x'][view], cursor['y'][view])
        if keydown(KEY_UP):
            if cursor['y'][view] != 0 if view == "white" else 7:
                if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                    erase_cursor(cursor['x'][view], cursor['y'][view])
                cursor['y'][view] += -1 if view == "white" else 1
                if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                    draw_cursor(cursor['x'][view], cursor['y'][view])
        if keydown(KEY_DOWN):
            if cursor['y'][view] != 7 if view == "white" else 0:
                if (cursor['x'][view], cursor['y'][view]) != (select['x'], select['y']):
                    erase_cursor(cursor['x'][view], cursor['y'][view])
                cursor['y'][view] += 1 if view == "white" else -1
                if (cursor['y'][view], cursor['y'][view]) != (select['x'], select['y']):
                    draw_cursor(cursor['x'][view], cursor['y'][view])
        # select inputs
        if keydown(KEY_OK):
            if selected:
                if (cursor['x'][view], cursor['y'][view]) in moves and get_piece_color(board[cursor['y'][view]][cursor['x'][view]]) != view:
                    # erase the piece from its original position
                    fill_case(select['x'], select['y'], get_case_color(select['x'], select['y']))

                    # updating board in consequence
                    piece = board[select['y']][select['x']]
                    board[cursor['y'][view]][cursor['x'][view]] = piece
                    board[select['y']][select['x']] = ""

                    # draw the piece in its new position
                    fill_case(cursor['x'][view], cursor['y'][view], get_case_color(cursor['x'][view], cursor['y'][view]))
                    draw_piece(cursor['x'][view], cursor['y'][view], piece)
                    draw_cursor(cursor['x'][view], cursor['y'][view])

                    # updating variables
                    select['x'], select['y'] = (None, None)
                    moves.clear()
                    selected = False
                    view = "black" if view == "white" else "white"
                
                else:
                    # erasing select in the last selected piece
                    erase_select(select['x'], select['y'])

                    # desabling select
                    draw_cursor(cursor['x'][view], cursor['y'][view])
                    select_x, select_y = (None, None)
                    selected = False
            else:
                # if selected case contains a piece it becomes the new selected piece
                if board[cursor['y'][view]][cursor['y'][view]] and get_piece_color(board[cursor['y'][view]][cursor['y'][view]]) == view:
                    select['x'], select['y'] = (cursor['x'][view], cursor['y'][view])
                    selected = True
                    # finding moves
                    moves = find_moves(select['x'], select['y'])
                    draw_select(select['x'], select['y'])
        time.sleep(0.1)
