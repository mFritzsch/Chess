import time
from collections import deque

import pygame

import pieces

pygame.init()

win = pygame.display.set_mode((850, 850))
pygame.display.set_caption("chess")


rounds = 0
run = True
board = [-0.5] * 64
move_board = [-0.5] * 64
last_moved = -1
game_over = False
x_search_depth = 3


def start_game(loc_board):
    for j in range(16):
        loc_board[48 + j] = j
    for j in range(16):
        loc_board[j] = -j - 1


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
                   white_pawn8, white_rook1, white_knight1, white_bishop1, white_queen, white_king, white_bishop2,
                   white_knight2, white_rook2,
                   black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7,
                   black_pawn8, black_rook1, black_knight1, black_bishop1, black_king, black_queen, black_bishop2,
                   black_knight2, black_rook2,
                   ]
all_sprites.add(existing_pieces)


def draw_board(loc_board):
    # draws the outlines of the board
    pygame.draw.rect(win, (255, 255, 255), (20, 20, 5, 810))
    pygame.draw.rect(win, (255, 255, 255), (825, 20, 5, 810))
    pygame.draw.rect(win, (255, 255, 255), (20, 20, 810, 5))
    pygame.draw.rect(win, (255, 255, 255), (20, 825, 810, 5))
    # draws the tiles of the board
    for i in range(8):
        for j in range(8):
            if (i*8+j) == last_moved:
                pygame.draw.rect(win, (255, 0, 0), (25 + 100 * j, 25 + 100 * i, 100, 100))
            elif (i + j) % 2 == 0:
                pygame.draw.rect(win, (255, 255, 255), (25 + 100 * j, 25 + 100 * i, 100, 100))
            else:
                pygame.draw.rect(win, (50, 50, 50), (25 + 100 * j, 25 + 100 * i, 100, 100))
            if loc_board[i*8+j] >= 0:
                existing_pieces[loc_board[i*8+j]].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if loc_board[i*8+j] <= -1:
                existing_pieces[loc_board[i*8+j]].set_x_and_y(25 + 100 * j, 25 + 100 * i)
            if loc_board[i*8+j] != -0.5:
                if existing_pieces[loc_board[i*8+j]].selected:
                    pygame.draw.rect(win, (255, 255, 51), (25 + 100 * j, 25 + 100 * i, 100, 100))
            if move_board[i*8+j] == -0.25 and (i+j) % 2 == 0:
                pygame.draw.rect(win, (0, 150, 0), (25 + 100 * j, 25 + 100 * i, 100, 100))
            elif move_board[i*8+j] == -0.25:
                pygame.draw.rect(win, (0, 125, 0), (25 + 100 * j, 25 + 100 * i, 100, 100))

    all_sprites.update()
    all_sprites.draw(win)


# removes moves from the move loc_board which allow a checkmate
def checkmate_prevent(loc_board, move_board, existing_pieces):
    for j in range(64):
        if loc_board[j] <= -1:
            if existing_pieces[loc_board[j]].selected:
                for i in range(len(move_board)):
                    if move_board[i] == -0.25:
                        test_board = loc_board[:]
                        test_board[i] = loc_board[j]
                        test_board[j] = -0.5
                        for a in range(len(test_board)):
                            if test_board[a] >= 0:
                                if a == 16 and i == 8:
                                    test_move_board = existing_pieces[test_board[a]].possible_moves(test_board, existing_pieces, a)
                                test_move_board = existing_pieces[test_board[a]].possible_moves(test_board,
                                                                                                existing_pieces, a)
                                for k in range(len(test_board)):
                                    if test_board[k] == -5:
                                        if test_move_board[k] == -0.25:
                                            move_board[i] = -0.5
        if loc_board[j] >= 0:
            if existing_pieces[loc_board[j]].selected:
                for i in range(len(move_board)):
                    if move_board[i] == -0.25:
                        test_board = loc_board[:]
                        test_board[i] = loc_board[j]
                        test_board[j] = -0.5
                        for a in range(len(test_board)):
                            if test_board[a] <= -1:
                                test_move_board = existing_pieces[test_board[a]].possible_moves(test_board, existing_pieces, a)
                                for k in range(len(test_board)):
                                    if test_board[k] == 12:
                                        if test_move_board[k] == -0.25:
                                            move_board[i] = -0.5
    return move_board


def promotion(position):
    if 0 <= position <= 7 and board[position] != -0.5 and isinstance(existing_pieces[board[position]], pieces.WhitePawn):
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
    elif 56 <= position <= 63 and board[position] != -0.5 and isinstance(existing_pieces[board[position]], pieces.BlackPawn):
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
                existing_pieces[board[position]] = pieces.BlackKnight()
            all_sprites.add(existing_pieces[board[position]])


# Adds castling moves to move_board if the conditions are met
def castling(move_board, rounds):
    queenside = False
    kingside = False
    if rounds % 2 == 0:
        if existing_pieces[8].move_counter == 0 and existing_pieces[12].move_counter == 0:
            if board[59] == -0.5 and board[58] == -0.5:
                queenside = True
                for i in range(64):
                    if board[i] <= -1:
                        potential_moves = existing_pieces[board[i]].possible_moves(board, existing_pieces, i)
                        if potential_moves[58] == -0.25 or potential_moves[59] == -0.25 or potential_moves[60] == -0.25:
                            queenside = False
        if existing_pieces[12].move_counter == 0 and existing_pieces[15].move_counter == 0:
            if board[61] == -0.5 and board[62] == -0.5:
                kingside = True
                for i in range(64):
                    if board[i] <= -1:
                        potential_moves = existing_pieces[board[i]].possible_moves(board, existing_pieces, i)
                        if potential_moves[60] == -0.25 or potential_moves[61] == -0.25 or potential_moves[62] == -0.25:
                            kingside = False
        if queenside:
            move_board[58] = -0.25
        if kingside:
            move_board[62] = -0.25
    else:
        if existing_pieces[24].move_counter == 0 and existing_pieces[27].move_counter == 0:
            if board[3] == -0.5 and board[2] == -0.5 and board[1] == -0.5:
                queenside = True
                for i in range(64):
                    if board[i] >= 0:
                        potential_moves = existing_pieces[board[i]].possible_moves(board, existing_pieces, i)
                        if potential_moves[2] == -0.25 or potential_moves[3] == -0.25 or potential_moves[4] == -0.25:
                            queenside = False
        if existing_pieces[27].move_counter == 0 and existing_pieces[31].move_counter == 0:
            if board[5] == -0.5 and board[6] == -0.5:
                kingside = True
                for i in range(64):
                    if board[i] >= 0:
                        potential_moves = existing_pieces[board[i]].possible_moves(board, existing_pieces, i)
                        if potential_moves[4] == -0.25 or potential_moves[5] == -0.25 or potential_moves[6] == -0.25:
                            kingside = False
        if queenside == True:
            move_board[2] = -0.25
        if kingside == True:
            move_board[6] = -0.25
    return move_board


# takes a positition on the board and either moves the selected piece to the square or
# selects the piece on the square if there is one
def move_piece(loc_board, move_board, existing_pieces, game_rounds, position):
    if move_board[position] == -0.25:
        for i in range(64):
            if loc_board[i] >= 0:
                if existing_pieces[loc_board[i]].selected:
                    if isinstance(existing_pieces[loc_board[i]], pieces.WhitePawn):
                        if position == i - 16:
                            existing_pieces[loc_board[i]].moved_two = True
                        elif position + 8 < 64 and loc_board[position + 8] != -0.5 and \
                                isinstance(existing_pieces[loc_board[position + 8]], pieces.BlackPawn) and \
                                existing_pieces[loc_board[position + 8]].moved_two:
                            loc_board[position + 8] = -0.5
                    if isinstance(existing_pieces[loc_board[i]], pieces.WhiteKing):
                        if position == i - 2:
                            loc_board[i - 1] = loc_board[56]
                            loc_board[56] = -0.5
                        if position == i + 2:
                            loc_board[i + 1] = loc_board[63]
                            loc_board[63] = -0.5
                    existing_pieces[loc_board[i]].selected = False
                    game_rounds += 1
                    loc_board[position] = loc_board[i]
                    loc_board[i] = -0.5
                    promotion(position)
                    move_board = [-0.5] * 64
                    break
            elif loc_board[i] <= -1:
                if existing_pieces[loc_board[i]].selected:
                    if isinstance(existing_pieces[loc_board[i]], pieces.BlackPawn):
                        if position == i + 16:
                            existing_pieces[loc_board[i]].moved_two = True
                        elif 0 <= position - 8 and loc_board[position - 8] != -0.5 and \
                                isinstance(existing_pieces[loc_board[position - 8]], pieces.WhitePawn) and \
                                existing_pieces[loc_board[position - 8]].moved_two:
                                        loc_board[position - 8] = -0.5
                    if isinstance(existing_pieces[loc_board[i]], pieces.BlackKing):
                        if position == i - 2:
                            loc_board[i - 1] = loc_board[0]
                            loc_board[0] = -0.5
                        if position == i + 2:
                            loc_board[i + 1] = loc_board[7]
                            loc_board[7] = -0.5
                    existing_pieces[loc_board[i]].selected = False
                    game_rounds += 1
                    loc_board[position] = loc_board[i]
                    loc_board[i] = -0.5
                    promotion(position)
                    move_board = [-0.5] * 64
                    break

    elif loc_board[position] != -0.5:
        for piece in existing_pieces:
            if piece.selected:
                piece.selected = False
                for square in move_board:
                    if square == -0.25:
                        square = -0.5
                break
        if existing_pieces[loc_board[position]].colour == "white" and game_rounds % 2 == 0 or \
                existing_pieces[loc_board[position]].colour == "black" and game_rounds % 2 != 0:
                    existing_pieces[loc_board[position]].selected = True
    for piece in existing_pieces:
        if piece.selected:
            move_board = piece.possible_moves(loc_board, existing_pieces, piece.get_x_and_y())
            move_board = checkmate_prevent(loc_board, move_board, existing_pieces)
            if isinstance(piece, pieces.WhiteKing) or isinstance(piece, pieces.BlackKing):
                move_board = castling(move_board, game_rounds)

    return loc_board, move_board, existing_pieces, game_rounds


def evaluate(loc_board, existing_pieces):
    score = 0
    for i in range(64):
        if loc_board[i] != -0.5:
            if isinstance(existing_pieces[loc_board[i]], pieces.White):
                score += existing_pieces[loc_board[i]].get_value(loc_board, i)
            else:
                score -= existing_pieces[loc_board[i]].get_value(loc_board, i)
    return score


def checkmate(loc_board, existing_pieces, rounds):
    for i in range(len(loc_board)):
        move_board = [-0.5] * 64
        for piece in existing_pieces:
            piece.selected = False
        if rounds % 2 == 0:
            if loc_board[i] >= 0:
                loc_board, move_board, existing_pieces, new_rounds = move_piece(loc_board, move_board, existing_pieces, rounds,
                                                                            i)
                for square in move_board:
                    if square == -0.25:
                        existing_pieces[loc_board[i]].selected = False
                        return False
        else:
            if loc_board[i] <= -1:
                existing_pieces[loc_board[i]].selected = True
                move_board = existing_pieces[loc_board[i]].possible_moves(loc_board, existing_pieces, i)
                move_board = checkmate_prevent(loc_board, move_board, existing_pieces)
                for square in move_board:
                    if square == -0.25:
                        existing_pieces[loc_board[i]].selected = False
                        return False
    for piece in existing_pieces:
        piece.selected = False
    return True


future_moves = [[0] * 64, [0] * 64]
def find_best_move(inp_board, existing_pieces, future_moves, alpha, beta, iteration, positions_calculated):
    gameover = checkmate(inp_board, existing_pieces, iteration)
    best_board = []
    potential_boards = deque()
    if iteration == 0 or gameover:
        return inp_board, future_moves, positions_calculated
    elif iteration == x_search_depth:
        # positive score because black wants to minimise
        score = 1000000
        for j in range(64):
            if inp_board[j] <= -1:
                move_board = existing_pieces[inp_board[j]].possible_moves(inp_board, existing_pieces, j)
                if isinstance(existing_pieces[inp_board[j]], pieces.BlackKing):
                    move_board = castling(move_board, iteration)
                for i in range(64):
                    for k in range(32):
                        existing_pieces[k].selected = False
                    existing_pieces[inp_board[j]].selected = True
                    move_board = checkmate_prevent(inp_board, move_board, existing_pieces)
                    temp_board, _, __, ___ = move_piece(inp_board[:], move_board[:], existing_pieces[:], 1, i)
                    if temp_board != inp_board:
                        potential_boards.append(temp_board)
        # sorting potential boards
        for i in range(len(potential_boards)-1):
            for j in range(len(potential_boards)-1):
                if evaluate(potential_boards[j], existing_pieces) > evaluate(potential_boards[j+1], existing_pieces):
                    potential_boards[j], potential_boards[j+1] = potential_boards[j+1], potential_boards[j]
        if inp_board == future_moves[0]:
            potential_boards.remove(future_moves[1])
            potential_boards.insert(0, future_moves[1])
        for i in range(len(potential_boards)):
            print(i)
            strongest_board, future_moves, positions_calculated = find_best_move(potential_boards[i][:], existing_pieces[:], future_moves, alpha, beta, iteration - 1, positions_calculated)
            if evaluate(strongest_board, existing_pieces) < score:
                score = evaluate(strongest_board, existing_pieces)
                best_board = potential_boards[i][:]
            beta = min(beta, evaluate(strongest_board, existing_pieces))
            if beta <= alpha:
                break
        for i in range(32):
            all_sprites.remove(existing_pieces[i])
        for i in range(64):
            if best_board[i] != -0.5:
                all_sprites.add(existing_pieces[best_board[i]])
        for i in range(len(existing_pieces)):
            existing_pieces[i].selected = False
        return best_board, future_moves, positions_calculated

    elif iteration % 2 == 0:
        # negative score because white wants to maximise
        score = -1000000
        for j in range(64):
            if inp_board[j] >= 0:
                move_board = existing_pieces[inp_board[j]].possible_moves(inp_board, existing_pieces, j)
                if isinstance(existing_pieces[inp_board[j]], pieces.WhiteKing):
                    move_board = castling(move_board, iteration)
                for i in range(64):
                    for k in range(32):
                        existing_pieces[k].selected = False
                    existing_pieces[inp_board[j]].selected = True
                    move_board = checkmate_prevent(inp_board, move_board, existing_pieces)
                    temp_board, _, __, ___ = move_piece(inp_board[:], move_board[:], existing_pieces[:], 1, i)
                    if temp_board != inp_board:
                        potential_boards.append(temp_board)
        # sorting potential boards
        for i in range(len(potential_boards)-1):
            for j in range(len(potential_boards)-1):
                if evaluate(potential_boards[j], existing_pieces) < evaluate(potential_boards[j+1], existing_pieces):
                    potential_boards[j], potential_boards[j+1] = potential_boards[j+1], potential_boards[j]
        for i in range(len(potential_boards)):
            strongest_board, future_moves, positions_calculated = find_best_move(potential_boards[i][:], existing_pieces[:], future_moves, alpha, beta, iteration - 1, positions_calculated)
            if score < evaluate(strongest_board, existing_pieces):
                best_board = strongest_board[:]
                score = evaluate(strongest_board, existing_pieces)
                if iteration == x_search_depth - 1:
                    future_moves[0] = best_board
            alpha = max(alpha, evaluate(strongest_board, existing_pieces))
            if beta <= alpha:
                return best_board, future_moves, positions_calculated
        return best_board, future_moves, positions_calculated

    else:
        # positive score because black wants to minimise
        score = 1000000
        for j in range(64):
            if inp_board[j] <= -1:
                move_board = existing_pieces[inp_board[j]].possible_moves(inp_board, existing_pieces, j)
                if isinstance(existing_pieces[inp_board[j]], pieces.BlackKing):
                    move_board = castling(move_board, iteration)
                for i in range(64):
                    for k in range(32):
                        existing_pieces[k].selected = False
                    existing_pieces[inp_board[j]].selected = True
                    move_board = checkmate_prevent(inp_board, move_board, existing_pieces)
                    temp_board, _, __, ___ = move_piece(inp_board[:], move_board[:], existing_pieces[:], 1, i)
                    if temp_board != inp_board:
                        potential_boards.append(temp_board)
        # sorting potential boards
        for i in range(len(potential_boards) - 1):
            for j in range(len(potential_boards) - 1):
                if evaluate(potential_boards[j], existing_pieces) > evaluate(potential_boards[j + 1],
                                                                             existing_pieces):
                    potential_boards[j], potential_boards[j + 1] = potential_boards[j + 1], potential_boards[j]
        for i in range(len(potential_boards)):
            if iteration == 1:
                positions_calculated += 1
            strongest_board, future_moves, positions_calculated = find_best_move(potential_boards[i][:], existing_pieces[:], future_moves, alpha,
                                                              beta, iteration - 1, positions_calculated)
            if score > evaluate(strongest_board, existing_pieces):
                best_board = strongest_board[:]
                score = evaluate(strongest_board, existing_pieces)
                if iteration == x_search_depth - 1:
                    future_moves[0] = best_board
            beta = min(beta, evaluate(strongest_board, existing_pieces))
            if beta <= alpha:
                return best_board, future_moves, positions_calculated
        return best_board, future_moves, positions_calculated


while game_over == 0:
    if rounds == 0:
        start_game(board)
    draw_board(board)
    pygame.display.update()
    if rounds % 2 == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                position = (int(x_pos / 100 - 0.25)) + 8 * (int(y_pos / 100 - 0.25))
                for i in range(len(existing_pieces)):
                    if existing_pieces[i].selected and existing_pieces[i].possible_moves(board, existing_pieces
                            , existing_pieces[i].get_x_and_y())[position] == -0.25:
                        existing_pieces[i].move_counter += 1
                if position < 64:
                    board, move_board, existing_pieces, new_rounds = move_piece(board, move_board, existing_pieces, rounds,
                                                                            position)
                else:
                    new_rounds = rounds
                if new_rounds == rounds + 1:
                    rounds = new_rounds
                    draw_board(board)
                    game_over = checkmate(board, existing_pieces, rounds)
                for i in range(32):
                    all_sprites.remove(existing_pieces[i])
                for i in range(64):
                    if board[i] != -0.5:
                        all_sprites.add(existing_pieces[board[i]])
                last_moved = -1
    else:
        for i in range(len(existing_pieces)):
            if (isinstance(existing_pieces[i], pieces.BlackPawn)):
                existing_pieces[i].moved_two = False
        prev_board = board[:]
        start = time.time()
        board, future_moves, positions_calculated = find_best_move(board, existing_pieces, future_moves, -1000000, 1000000,
                                             x_search_depth, 0)
        end = time.time()
        print("time elapsed:", end-start)
        print(positions_calculated)
        rounds += 1
        game_over = checkmate(board, existing_pieces, rounds)

        for i in range(len(board)):
            if board[i] != -0.5 and board[i] != prev_board[i]:
                last_moved = i
        if board[4] != -5:
            existing_pieces[-5].move_counter = 1
        if board[0] != -1:
            existing_pieces[-1].move_counter = 1
            if board[7] != -8:
                existing_pieces[-8].move_counter = 1
    for i in range(32):
        if rounds % 2 == 0:
            if isinstance(existing_pieces[i], pieces.WhitePawn):
                existing_pieces[i].moved_two = False
        else:
            if isinstance(existing_pieces[i], pieces.BlackPawn):
                existing_pieces[i].moved_two = False

pygame.quit()