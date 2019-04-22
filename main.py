import pygame
import pieces

pygame.init()

win = pygame.display.set_mode((850, 850))
pygame.display.set_caption("chess")

rounds = 0
run = True
board = [-0.5] * 64
move_board = [-0.5] * 64


def start_game(board):
    for i in range(16):
        board[48 + i] = i
    for i in range(16):
        board[i] = -i - 1


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


def check_square(pos):
    if board[pos] <= -1:
        piece = existing_pieces[board[pos] ]
        return piece
    elif board[pos] >= 0:
        piece = existing_pieces[board[pos] ]
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
                pygame.draw.rect(win, (255, 255, 255), (25 + 100 * j, 25 + 100 * i, 100, 100))
            else:
                pygame.draw.rect(win, (50, 50, 50), (25 + 100 * j, 25 + 100 * i, 100, 100))
            if board[i*8+j] >= 0:
                existing_pieces[board[i*8+j]].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if board[i*8+j] <= -1:
                existing_pieces[board[i*8+j]].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if board[i*8+j] != -0.5:
                if existing_pieces[board[i*8+j]].selected:
                    pygame.draw.rect(win, (255, 255, 51), (25 + 100 * j, 25 + 100 * i, 100, 100))
            if move_board[i*8+j] == -0.25 and (i+j) % 2 == 0:
                pygame.draw.rect(win, (0, 150, 0), (25 + 100 * j, 25 + 100 * i, 100, 100))
            elif move_board[i*8+j] == -0.25:
                pygame.draw.rect(win, (0, 125, 0), (25 + 100 * j, 25 + 100 * i, 100, 100))

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


def checkmate_prevent(board, move_board, existing_pieces):
    for j in range(len(board)):
        if board[j] <= -1:
            if existing_pieces[board[j]].selected:
                for i in range(len(move_board)):
                    if move_board[i] == -0.25:
                        test_board = board[:]
                        test_board[i] = board[j]
                        test_board[j] = -0.5
                        for a in range(len(test_board)):
                            if test_board[a] >= 0:
                                test_move_board = existing_pieces[test_board[a]].possible_moves(test_board)
                                for k in range(len(test_board)):
                                    if test_board[k] == -5:
                                        if test_move_board[k] == -0.25:
                                            move_board[i] = -0.5
        if board[j] >= 0:
            if existing_pieces[board[j]].selected:
                for i in range(len(move_board)):
                    if move_board[i] == -0.25:
                        test_board = board[:]
                        test_board[i] = board[j]
                        test_board[j] = -0.5
                        for a in range(len(test_board)):
                            if test_board[a] <= -1:
                                test_move_board = existing_pieces[test_board[a]].possible_moves(test_board)
                                for k in range(len(test_board)):
                                    if test_board[k] == 12:
                                        if test_move_board[k] == -0.25:
                                            move_board[i] = -0.5
    return move_board





def move_piece(board, move_board, existing_pieces, rounds):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            position = (int(x_pos / 100 - 0.25)) + 8 * (int(y_pos / 100 - 0.25))
            if position < 64:
                if move_board[position] == -0.25:
                    for i in range(len(board)):
                        if board[i] >= 0:
                            if existing_pieces[board[i]].selected:
                                existing_pieces[board[i]].selected = False
                                rounds += 1
                                if board[position] != -0.5:
                                    all_sprites.remove(existing_pieces[board[position]])
                                board[position] = board[i]
                                board[i] = -0.5
                                if isinstance(existing_pieces[board[position]], pieces.WhitePawn):
                                    if 0 <= position <= 7:
                                        user_input = -1
                                        while user_input < 1 or user_input > 4:
                                            user_input = int(input("enter 1 for Rook, 2 for Queen, 3 for Bishop and "
                                                               "4 for Knight"))
                                            all_sprites.remove(existing_pieces[board[position]])
                                            if user_input == 1:
                                                existing_pieces[board[position]] = pieces.WhiteRook()
                                            elif user_input == 2:
                                                existing_pieces[board[position]] = pieces.WhiteQueen()
                                            elif user_input == 3:
                                                existing_pieces[board[position]] = pieces.WhiteBishop()
                                            elif user_input == 4:
                                                existing_pieces[board[position]] = pieces.WhiteKnight()
                                            all_sprites.add(existing_pieces[board[position]])
                                move_board = [0] * 64
                                break
                        elif board[i] <= -1:
                            if existing_pieces[board[i]].selected:
                                existing_pieces[board[i]].selected = False
                                rounds += 1
                                if board[position] != -0.5:
                                    all_sprites.remove(existing_pieces[board[position]])
                                board[position] = board[i]
                                board[i] = -0.5
                                if 54 <= position <= 63 and isinstance(existing_pieces[board[position]], pieces.BlackPawn):
                                    user_input = -1
                                    while user_input < 1 or user_input > 4:
                                        user_input = int(input("enter 1 for Rook, 2 for Queen, 3 for Bishop and "
                                                           "4 for Knight"))
                                        all_sprites.remove(existing_pieces[board[position]])
                                        if user_input == 1:
                                            existing_pieces[board[position]] = pieces.BlackRook()
                                        elif user_input == 2:
                                            existing_pieces[board[position]] = pieces.BlackQueen()
                                        elif user_input == 3:
                                            existing_pieces[board[position]] = pieces.BlackBishop()
                                        elif user_input == 4:
                                            existing_pieces[board[position]] = pieces.BlackKinght()
                                        all_sprites.add(existing_pieces[board[position]])


                                move_board = [0] * 64
                                break

                elif board[position] != -0.5:
                    for i in range(len(existing_pieces)):
                        if existing_pieces[i].selected:
                            existing_pieces[i].selected = False
                            for j in range(len(move_board)):
                                if move_board[j] == -0.25:
                                    move_board[j] = -0.5
                    if check_square(position).colour == "white" and rounds % 2 == 0 or \
                            check_square(position).colour == "black" and rounds % 2 != 0:
                        check_square(position).selected = True
    for i in range(len(existing_pieces)):
        if existing_pieces[i].selected:

            move_board = existing_pieces[i].possible_moves(board)
            move_board = checkmate_prevent(board, move_board, existing_pieces)

    return board, move_board, existing_pieces, rounds

while True:
    if rounds == 0:
        start_game(board)
    draw_board()
    pygame.display.update()
    board, move_board, existing_pieces, rounds = move_piece(board, move_board, existing_pieces, rounds)

# pygame.quit()
