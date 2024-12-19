import pygame
from .constants import BLACK, WHITE, ROWS, COLS, SQUARE_SIZE, BORDER_THICKNESS

class Board:
    def __init__(self):
        self.board = []
        # self.create_board()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), BORDER_THICKNESS)

    def create_board(self):
        pass

    def draw(self, win):
        pass