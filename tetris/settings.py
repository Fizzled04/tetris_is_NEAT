import pygame

COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

YELLOW = '#f1e60d'
RED = '#e51b20'
BLUE = '#204b9b'
GREEN = '#65b32e'
PURPLE = '7b217f'
ORANGE = '#f07e13'
CYAN = '#1C1C1C'
LINE_COLOR = '#FFFFFF'

TETROMINOS = {
    'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': PURPLE},
    'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': YELLOW},
    'J': {'shape': [(0, 0), (0, -1), (0, 1), (-1, 1)], 'color': BLUE},
    'L': {'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': ORANGE},
    'I': {'shape': [(0, 0), (0, -1), (0, -2), (0, 1)], 'color': CYAN},
    'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': GREEN},
    'Z': {'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': RED}
}