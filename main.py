import pygame
import pieces

pygame.init()

win = pygame.display.set_mode((850, 850))
pygame.display.set_caption("chess")

rounds = 0
run = True
board = [0] * 64
move_board = [0] * 64


def start_game(board):
    for i in range(16):
        board[48 + i] = i + 2
    for i in range(16):
        board[i] = -i - 3


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
existing_pieces = [white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                   white_pawn8, white_rook1, white_knight1, white_bishop1, white_queen, white_king,white_bishop2,
                   white_knight2, white_rook2,
                   black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7,
                   black_pawn8, black_rook1, black_knight1, black_bishop1, black_king, black_queen, black_bishop2,
                   black_knight2, black_rook2,
                   ]
all_sprites.add(existing_pieces)


def check_square(x, y):
    if board[int(x / 100) + 8 * (int(y / 100))] < -1:
        piece = existing_pieces[board[(int(x / 100)) + 8 * (int(y / 100))] + 2]
        return piece
    elif board[int(x / 100) + 8 * (int(y / 100))] > 1:
        piece = existing_pieces[board[(int(x / 100)) + 8 * (int(y / 100))] - 2]
        return piece


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
            if board[i*8+j] > 1:
                existing_pieces[board[i*8+j] - 2].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if board[i*8+j] < -1:
                existing_pieces[board[i*8+j] + 2].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if move_board[i+8*j] == 1:
                pygame.draw.rect(win, (200, 0, 0), (25 + 100 * i, 25 + 100 * j, 100, 100))

    all_sprites.update()
    all_sprites.draw(win)


# do I need this?
def hostile(a, b):
    if a.colour == "white":
        if b.colour == "black":
            return True
    else:
        if b.colour == "white":
            return True


def move_piece(board, move_board, existing_pieces, rounds):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            if (int(x_pos / 100)) + 8 * (int(y_pos / 100)) < 64:
                if move_board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] == 1:
                    rounds += 1
                    for i in range(len(board)):
                        if board[i] > 0:
                            if existing_pieces[board[i]-2].selected:
                                existing_pieces[board[i]-2].selected = False
                                if board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] != 0:
                                    all_sprites.remove(existing_pieces[board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] + 2])
                                board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] = board[i]
                                board[i] = 0
                                for j in range(len(move_board)):
                                    if move_board[j] == 1:
                                        move_board[j] = 0
                                break
                        else:
                            if existing_pieces[board[i]+2].selected:
                                existing_pieces[board[i]+2].selected = False
                                if board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] != 0:
                                    all_sprites.remove(existing_pieces[board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] - 2])
                                board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] = board[i]
                                board[i] = 0
                                for j in range(len(move_board)):
                                    if move_board[j] == 1:
                                        move_board[j] = 0
                                break

                elif board[(int(x_pos / 100)) + 8 * (int(y_pos / 100))] != 0:
                    for i in range(len(existing_pieces)):
                        if existing_pieces[i].selected:
                            existing_pieces[i].selected = False
                            for j in range(len(move_board)):
                                if move_board[j] == 1:
                                    move_board[j] = 0
                    if check_square(x_pos, y_pos).colour == "white" and rounds % 2 == 0 or \
                            check_square(x_pos, y_pos).colour == "black" and rounds % 2 != 0:
                        check_square(x_pos, y_pos).selected = True
    for i in range(len(existing_pieces)):
        if existing_pieces[i].selected:


            move_board = existing_pieces[i].possible_moves(board)
            for j in range(len(move_board)):
                if move_board[j] != 0 and move_board[j] != 1:
                    move_board[j] = 0
    return board, move_board, existing_pieces, rounds

while True:
    if rounds == 0:
        start_game(board)
    draw_board()
    pygame.display.update()
    board, move_board, existing_pieces, rounds = move_piece(board, move_board, existing_pieces, rounds)
    if rounds % 1 == 0:
        # print(move_board)
        # print(board)
        for i in range(len(board)):
            #print(existing_pieces[board[i]].selected)
            continue
    for i in range(len(existing_pieces)):
        if existing_pieces[i].selected:
            # print(i)
            continue

pygame.quit()
