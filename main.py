import pygame

pygame.init()

win = pygame.display.set_mode((850, 850))
pygame.display.set_caption("chess")

rounds = 0
run = True
board_pieces = [-1] * 64
pieces = [pygame.image.load("sprites/white_king.png"), pygame.image.load("sprites/white_queen.png"),
          pygame.image.load("sprites/white_bishop.png"), pygame.image.load("sprites/white_knight.png"),
          pygame.image.load("sprites/white_rook.png"), pygame.image.load("sprites/white_pawn.png")]

def start_game(board_pieces):
    for i in range(8):
        board_pieces[49 + i] = 5
    board_pieces[56] = 4
    board_pieces[63] = 4
    board_pieces[57] = 3
    board_pieces[62] = 3
    board_pieces[58] = 2
    board_pieces[61] = 2
    board_pieces[59] = 1
    board_pieces[60] = 0

def draw_board():
    # draws the outlines of the board
    pygame.draw.rect(win, (255, 255, 255), (20, 20, 5, 810))
    pygame.draw.rect(win, (255, 255, 255), (825, 20, 5, 810))
    pygame.draw.rect(win, (255, 255, 255), (20, 20, 810, 5))
    pygame.draw.rect(win, (255, 255, 255), (20, 825, 810, 5))
    # draws the tiles of the board
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(win, (255, 255, 255), (25 + 100 * i, 25 + 100 * j, 100, 100))
            if board_pieces[i*j] != -1:
                win.blit(pieces[board_pieces[i*j]], (i, j))
while True:
    if rounds == 0:
        start_game(board_pieces)
    draw_board()
    pygame.display.update()
pygame.quit()

# sizes:
# king=77*80
# queen=82*80
# bishop=89*80
# knight=88*80
# rook=85*80
# pawn=82*80

