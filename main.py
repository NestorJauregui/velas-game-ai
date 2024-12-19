import pygame
from velas.constants import WIDTH, HEIGHT
from velas.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption("Velas")

def main():

    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():

            # Quit the game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw_squares(WIN)
        pygame.display.update()
    
    pygame.quit()

main()