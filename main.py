import pygame
import pieces

pygame.init()

win = pygame.display.set_mode((850, 850))
pygame.display.set_caption("chess")

rounds = 0
run = True
board_pieces = [-1] * 64


def start_game(board_pieces):
    for i in range(16):
        board_pieces[48 + i] = i +2
    for i in range(16):
        board_pieces[i] = -i -3


white_king = pieces.WhiteKing()
white_queen = pieces.WhiteQueen()
white_bishop1 = pieces.WhiteBishop()
white_bishop2 = pieces.WhiteBishop()
white_knight1 = pieces.WhiteKnight()
white_knight2 = pieces.WhiteKnight()
white_rook1 = pieces.WhiteRook()
white_rook2 = pieces.WhiteRook()
white_pawn1 = pieces.WhitePawn()
white_pawn2 = pieces.WhitePawn()
white_pawn3 = pieces.WhitePawn()
white_pawn4 = pieces.WhitePawn()
white_pawn5 = pieces.WhitePawn()
white_pawn6 = pieces.WhitePawn()
white_pawn7 = pieces.WhitePawn()
white_pawn8 = pieces.WhitePawn()

black_king = pieces.BlackKing()
black_queen = pieces.BlackQueen()
black_bishop1 = pieces.BlackBishop()
black_bishop2 = pieces.BlackBishop()
black_knight1 = pieces.BlackKnight()
black_knight2 = pieces.BlackKnight()
black_rook1 = pieces.BlackRook()
black_rook2 = pieces.BlackRook()
black_pawn1 = pieces.BlackPawn()
black_pawn2 = pieces.BlackPawn()
black_pawn3 = pieces.BlackPawn()
black_pawn4 = pieces.BlackPawn()
black_pawn5 = pieces.BlackPawn()
black_pawn6 = pieces.BlackPawn()
black_pawn7 = pieces.BlackPawn()
black_pawn8 = pieces.BlackPawn()

all_sprites = pygame.sprite.Group()
existing_pieces = [white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5,
                   white_pawn6, white_pawn7, white_pawn8, white_rook1, white_knight1, white_queen, white_king,
                   white_bishop1, white_knight2, white_bishop2, white_rook2,
                   black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5,
                   black_pawn6, black_pawn7, black_pawn8, black_rook1, black_knight1, black_queen, black_king,
                   black_bishop1, black_knight2, black_bishop2, black_rook2,
                   ]
all_sprites.add(existing_pieces)


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
            else:
                pygame.draw.rect(win, (50, 50, 50), (25 + 100 * i, 25 + 100 * j, 100, 100))
            if board_pieces[i*8+j] > 1:
                existing_pieces[board_pieces[i*8+j] - 2].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if board_pieces[i*8+j] < -1:
                existing_pieces[board_pieces[i*8+j] + 2].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if board_pieces[i+8*j] == 1:
                pygame.draw.rect(win, (200, 0, 0), (25 + 100 * i, 25 + 100 * j, 100, 100))

    all_sprites.draw(win)
    all_sprites.update()
while True:
    if rounds == 0:
        start_game(board_pieces)
    draw_board()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            if (int(x_pos / 100)) + 8 * (int(y_pos / 100)) < 64:
                board_pieces = existing_pieces[board_pieces[(int(x_pos / 100)) + 8 * (int(y_pos / 100))]].possible_moves(board_pieces)
pygame.quit()

