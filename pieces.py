import pygame


class AnyPiece(pygame.sprite.Sprite):
    def __init__(self):
        self.selected = False
        self.move_counter = 0

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    def get_value(self, board, position):
        return self.point_value + self.piece_square_table[position]


class White(AnyPiece):
    def __init__(self):
        AnyPiece.__init__(self)
        self.colour = "white"


class Black(AnyPiece):
    def __init__(self):
        AnyPiece.__init__(self)
        self.colour = "black"


class BlackKing(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_king.png")
        self.rect = self.image.get_rect()
        self.point_value = 20000
        self.piece_square_table = [20, 30, 10, 0, 0, 10, 30, 20,
                                   20, 20, 0, 0, 0, 0, 20, 20,
                                   -10, -20, -20, -20, -20, -20, -20, -10,
                                   -20, -30, -30, -40, -40, -30, -30, -20,
                                   -30, -40, -40, -50, -50, -40, -40, -30,
                                   -30, -40, -40, -50, -50, -40, -40, -30,
                                   -30, -40, -40, -50, -50, -40, -40, -30,
                                   -30, -40, -40, -50, -50, -40, -40, -30]

        self.endgame_piece_square_table = [-50, -30, -30, -30, -30, -30, -30, -50,
                                           - 30, -30, 0, 0, 0, 0, -30, -30,
                                           -30, -10, 20, 30, 30, 20, -10, -30,
                                           -30, -10, 30, 40, 40, 30, -10, -30,
                                           -30, -10, 30, 40, 40, 30, -10, -30,
                                           -30, -10, 20, 30, 30, 20, -10, -30,
                                           -30, -20, -10, 0, 0, -10, -20, -30,
                                           -50, -40, -30, -20, -20, -30, -40, -50]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        for i in range(3):
            for j in range(3):
                if 0 <= (x + y * 8 - 9) + i + 8 * j < 64 and 8 > (x-1) + i > -1:
                    if move_board[(x + y * 8 - 9) + i + 8 * j] == -0.5 or move_board[(x + y * 8 - 9) + i + 8 * j] >= 0:
                        move_board[(x + y * 8 - 9) + i + 8 * j] = -0.25
        return move_board

    def get_value(self, board, position):
        for i in range(len(board)):
            if board[i] == 28 or board[i] == 11:
                return self.point_value + self.piece_square_table[position]
        return self.point_value + self.endgame_piece_square_table[position]


class WhiteKing(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_king.png")
        self.rect = self.image.get_rect()
        self.point_value = 20000
        self.piece_square_table = [-30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -20,-30,-30,-40,-40,-30,-30,-20,
                                    -10,-20,-20,-20,-20,-20,-20,-10,
                                     20, 20,  0,  0,  0,  0, 20, 20,
                                     20, 30, 10,  0,  0, 10, 30, 20]
        self.endgame_piece_square_table = [-50,-40,-30,-20,-20,-30,-40,-50,
                                            -30,-20,-10,  0,  0,-10,-20,-30,
                                            -30,-10, 20, 30, 30, 20,-10,-30,
                                            -30,-10, 30, 40, 40, 30,-10,-30,
                                            -30,-10, 30, 40, 40, 30,-10,-30,
                                            -30,-10, 20, 30, 30, 20,-10,-30,
                                            -30,-30,  0,  0,  0,  0,-30,-30,
                                            -50,-30,-30,-30,-30,-30,-30,-50]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        for i in range(3):
            for j in range(3):
                if 0 <= (x + y * 8 - 9) + i + 8 * j < 64 and 8 > (x-1) + i > -1:
                    if move_board[(x + y * 8 - 9) + i + 8 * j] == -0.5 or move_board[(x + y * 8 - 9) + i + 8 * j] <= -1:
                        move_board[(x + y * 8 - 9) + i + 8 * j] = -0.25
        return move_board

    def get_value(self, board, position):
        for i in range(len(board)):
            if board[i] == 28 or board[i] == 11:
                return self.point_value + self.piece_square_table[position]
        return self.point_value + self.endgame_piece_square_table[position]


class BlackQueen(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_queen.png")
        self.rect = self.image.get_rect()
        self.point_value = 900
        self.piece_square_table = [-20, -10, -10, -5, -5, -10, -10, -20,
                                   -10, 0, 5, 0, 0, 0, 0, -10,
                                   -10, 5, 5, 5, 5, 5, 0, -10,
                                   0, 0, 5, 5, 5, 5, 0, -5,
                                   -5, 0, 5, 5, 5, 5, 0, -5,
                                   -10, 0, 5, 5, 5, 5, 0, -10,
                                   -10, 0, 0, 0, 0, 0, 0, -10,
                                   -20, -10, -10, -5, -5, -10, -10, -20]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        for i in range(y):
            if move_board[((x + y * 8) - 8 * (i + 1))] == -0.5:
                move_board[((x + y * 8) - 8 * (i + 1))] = -0.25
            elif move_board[((x + y * 8) - 8 * (i + 1))] >= 0:
                move_board[((x + y * 8) - 8 * (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) - 8 * (i + 1))] <= -1:
                break

        for i in range(7 - x):
            if move_board[((x + y * 8) + (i + 1))] == -0.5:
                move_board[((x + y * 8) + (i + 1))] = -0.25
            elif move_board[((x + y * 8) + (i + 1))] >= 0:
                move_board[((x + y * 8) + (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) + (i + 1))] <= -1:
                break

        for i in range(7 - y):
            if move_board[((x + y * 8) + 8 * (i + 1))] == -0.5:
                move_board[((x + y * 8) + 8 * (i + 1))] = -0.25
            elif move_board[((x + y * 8) + 8 * (i + 1))] >= 0:
                move_board[((x + y * 8) + 8 * (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) + 8 * (i + 1))] <= -1:
                break

        for i in range(x):
            if move_board[((x + y * 8) - (i + 1))] == -0.5:
                move_board[((x + y * 8) - (i + 1))] = -0.25
            elif move_board[((x + y * 8) - (i + 1))] >= 0:
                move_board[((x + y * 8) - (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) - (i + 1))] <= -1:
                break

        for i in range(8):
            if 0 <= (x + y * 8) + (i + 1) * 9 < 64 and x + (i + 1) < 8:
                if move_board[(x + y * 8) + (i + 1) * 9] == -0.5:
                    move_board[(x + y * 8) + (i + 1) * 9] = -0.25
                if move_board[(x + y * 8) + (i + 1) * 9] >= 0:
                    move_board[(x + y * 8) + (i + 1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) + (i + 1) * 9] <= -1:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) - (i + 1) * 9 < 64 and x - (i + 1) > -1:
                if move_board[(x + y * 8) - (i + 1) * 9] == -0.5:
                    move_board[(x + y * 8) - (i + 1) * 9] = -0.25
                if move_board[(x + y * 8) - (i + 1) * 9] >= 0:
                    move_board[(x + y * 8) - (i + 1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) - (i + 1) * 9] <= -1:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) + (i + 1) * 7 < 64 and x - (i + 1) > -1:
                if move_board[(x + y * 8) + (i + 1) * 7] == -0.5:
                    move_board[(x + y * 8) + (i + 1) * 7] = -0.25
                if move_board[(x + y * 8) + (i + 1) * 7] >= 0:
                    move_board[(x + y * 8) + (i + 1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) + (i + 1) * 7] <= -1:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) - (i + 1) * 7 < 64 and x + (i + 1) < 8:
                if move_board[(x + y * 8) - (i + 1) * 7] == -0.5:
                    move_board[(x + y * 8) - (i + 1) * 7] = -0.25
                if move_board[(x + y * 8) - (i + 1) * 7] >= 0:
                    move_board[(x + y * 8) - (i + 1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) - (i + 1) * 7] <= -1:
                    break

        return move_board


class WhiteQueen(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_queen.png")
        self.rect = self.image.get_rect()
        self.point_value = 900
        self.piece_square_table = [-20,-10,-10, -5, -5,-10,-10,-20,
                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                    -10,  0,  5,  5,  5,  5,  0,-10,
                                     -5,  0,  5,  5,  5,  5,  0, -5,
                                      0,  0,  5,  5,  5,  5,  0, -5,
                                    -10,  5,  5,  5,  5,  5,  0,-10,
                                    -10,  0,  5,  0,  0,  0,  0,-10,
                                    -20,-10,-10, -5, -5,-10,-10,-20]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        for i in range(y):
            if move_board[((x + y * 8) - 8 * (i+1))] == -0.5:
                move_board[((x + y * 8) - 8 * (i+1))] = -0.25
            elif move_board[((x + y * 8) - 8 * (i+1))] <= -1:
                move_board[((x + y * 8) - 8 * (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) - 8 * (i+1))] >= 0:
                break

        for i in range(7 - x):
            if move_board[((x + y * 8) + (i+1))] == -0.5:
                move_board[((x + y * 8) + (i+1))] = -0.25
            elif move_board[((x + y * 8) + (i+1))] <= -1:
                move_board[((x + y * 8) + (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) + (i+1))] >= 0:
                break

        for i in range(7 - y):
            if move_board[((x + y * 8) + 8 * (i+1))] == -0.5:
                move_board[((x + y * 8) + 8 * (i+1))] = -0.25
            elif move_board[((x + y * 8) + 8 * (i+1))] <= -1:
                move_board[((x + y * 8) + 8 * (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) + 8 * (i+1))] >= 0:
                break

        for i in range(x):
            if move_board[((x + y * 8) - (i+1))] == -0.5:
                move_board[((x + y * 8) - (i+1))] = -0.25
            elif move_board[((x + y * 8) - (i+1))] <= -1:
                move_board[((x + y * 8) - (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) - (i+1))] >= 0:
                break

        for i in range(8):
            if 0 <= (x + y * 8) + (i+1) * 9 < 64 and x + (i+1) < 8:
                if move_board[(x + y * 8) + (i+1) * 9] == -0.5:
                    move_board[(x + y * 8) + (i+1) * 9] = -0.25
                if move_board[(x + y * 8) + (i+1) * 9] <= -1:
                    move_board[(x + y * 8) + (i+1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) + (i+1) * 9] >= 0:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) - (i+1) * 9 < 64 and x - (i+1) > -1:
                if move_board[(x + y * 8) - (i+1) * 9] == -0.5:
                    move_board[(x + y * 8) - (i+1) * 9] = -0.25
                if move_board[(x + y * 8) - (i+1) * 9] <= -1:
                    move_board[(x + y * 8) - (i+1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) - (i+1) * 9] >= 0:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) + (i+1) * 7 < 64 and x - (i+1) > -1:
                if move_board[(x + y * 8) + (i+1) * 7] == -0.5:
                    move_board[(x + y * 8) + (i+1) * 7] = -0.25
                if move_board[(x + y * 8) + (i+1) * 7] <= -1:
                    move_board[(x + y * 8) + (i+1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) + (i+1) * 7] >= 0:
                    break
        for i in range(8):
            if 0 <= (x + y * 8) - (i+1) * 7 >= 0 < 64 and x + (i+1) < 8:
                if move_board[(x + y * 8) - (i+1) * 7] == -0.5:
                    move_board[(x + y * 8) - (i+1) * 7] = -0.25
                if move_board[(x + y * 8) - (i+1) * 7] <= -1:
                    move_board[(x + y * 8) - (i+1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) - (i+1) * 7] >= 0:
                    break
        return move_board


class BlackBishop(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_bishop.png")
        self.rect = self.image.get_rect()
        self.point_value = 330
        self.piece_square_table = [-20, -10, -10, -10, -10, -10, -10, -20,
                                   -10, 5, 0, 0, 0, 0, 5, -10,
                                   -10, 10, 10, 10, 10, 10, 10, -10,
                                   -10, 0, 10, 10, 10, 10, 0, -10,
                                   -10, 5, 5, 10, 10, 5, 5, -10,
                                   -10, 0, 5, 10, 10, 5, 0, -10,
                                   -10, 0, 0, 0, 0, 0, 0, -10,
                                   -20, -10, -10, -10, -10, -10, -10, -20]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        for i in range(8):
            if 0 <= (x + y * 8) + (i+1) * 9 < 64 and x + (i+1) < 8:
                if move_board[(x + y * 8) + (i+1) * 9] == -0.5:
                    move_board[(x + y * 8) + (i+1) * 9] = -0.25
                if move_board[(x + y * 8) + (i+1) * 9] >= 0:
                    move_board[(x + y * 8) + (i+1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) + (i+1) * 9] <= -1:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) - (i+1) * 9 < 64 and x - (i+1) > -1:
                if move_board[(x + y * 8) - (i+1) * 9] == -0.5:
                    move_board[(x + y * 8) - (i+1) * 9] = -0.25
                if move_board[(x + y * 8) - (i+1) * 9] >= 0:
                    move_board[(x + y * 8) - (i+1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) - (i+1) * 9] <= -1:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) + (i+1) * 7 < 64 and x - (i+1) > -1:
                if move_board[(x + y * 8) + (i+1) * 7] == -0.5:
                    move_board[(x + y * 8) + (i+1) * 7] = -0.25
                if move_board[(x + y * 8) + (i+1) * 7] >= 0:
                    move_board[(x + y * 8) + (i+1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) + (i+1) * 7] <= -1:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) - (i+1) * 7 < 64 and x + (i+1) < 8:
                if move_board[(x + y * 8) - (i+1) * 7] == -0.5:
                    move_board[(x + y * 8) - (i+1) * 7] = -0.25
                if move_board[(x + y * 8) - (i+1) * 7] >= 0:
                    move_board[(x + y * 8) - (i+1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) - (i+1) * 7] <= -1:
                    break

        return move_board


class WhiteBishop(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_bishop.png")
        self.rect = self.image.get_rect()
        self.point_value = 330
        self.piece_square_table = [-20,-10,-10,-10,-10,-10,-10,-20,
                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                    -10,  0,  5, 10, 10,  5,  0,-10,
                                    -10,  5,  5, 10, 10,  5,  5,-10,
                                    -10,  0, 10, 10, 10, 10,  0,-10,
                                    -10, 10, 10, 10, 10, 10, 10,-10,
                                    -10,  5,  0,  0,  0,  0,  5,-10,
                                    -20,-10,-10,-10,-10,-10,-10,-20]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        for i in range(8):
            if 0 <= (x + y * 8) + (i + 1) * 9 < 64 and x + (i + 1) < 8:
                if move_board[(x + y * 8) + (i + 1) * 9] == -0.5:
                    move_board[(x + y * 8) + (i + 1) * 9] = -0.25
                if move_board[(x + y * 8) + (i + 1) * 9] <= -1:
                    move_board[(x + y * 8) + (i + 1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) + (i + 1) * 9] >= 0:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) - (i + 1) * 9 < 64 and x - (i + 1) > -1:
                if move_board[(x + y * 8) - (i + 1) * 9] == -0.5:
                    move_board[(x + y * 8) - (i + 1) * 9] = -0.25
                if move_board[(x + y * 8) - (i + 1) * 9] <= -1:
                    move_board[(x + y * 8) - (i + 1) * 9] = -0.25
                    break
                if move_board[(x + y * 8) - (i + 1) * 9] >= 0:
                    break

        for i in range(8):
            if 0 <= (x + y * 8) + (i + 1) * 7 < 64 and x - (i + 1) > -1:
                if move_board[(x + y * 8) + (i + 1) * 7] == -0.5:
                    move_board[(x + y * 8) + (i + 1) * 7] = -0.25
                if move_board[(x + y * 8) + (i + 1) * 7] <= -1:
                    move_board[(x + y * 8) + (i + 1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) + (i + 1) * 7] >= 0:
                    break
        for i in range(8):
            if 0 <= (x + y * 8) - (i + 1) * 7 >= 0 < 64 and x + (i + 1) < 8:
                if move_board[(x + y * 8) - (i + 1) * 7] == -0.5:
                    move_board[(x + y * 8) - (i + 1) * 7] = -0.25
                if move_board[(x + y * 8) - (i + 1) * 7] <= -1:
                    move_board[(x + y * 8) - (i + 1) * 7] = -0.25
                    break
                if move_board[(x + y * 8) - (i + 1) * 7] >= 0:
                    break

        return move_board


class BlackKnight(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_knight.png")
        self.rect = self.image.get_rect()
        self.point_value = 320
        self.piece_square_table = [-50, -40, -30, -30, -30, -30, -40, -50,
                                   -40, -20, 0, 5, 5, 0, -20, -40,
                                   -30, 5, 10, 15, 15, 10, 5, -30,
                                   -30, 0, 15, 20, 20, 15, 0, -30,
                                   -30, 5, 15, 20, 20, 15, 5, -30,
                                   -30, 0, 10, 15, 15, 10, 0, -30,
                                   -40, -20, 0, 0, 0, 0, -20, -40,
                                   -50, -40, -30, -30, -30, -30, -40, -50]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        if x < 6:
            if (x + 8 * y) + 10 <= 63:
                if move_board[(x + 8 * y) + 10] == -0.5 or move_board[(x + 8 * y) + 10] >= 0:
                    move_board[(x + 8 * y) + 10] = -0.25
            if (x + 8 * y) - 6 > 0:
                if move_board[(x + 8 * y) - 6] == -0.5 or move_board[(x + 8 * y) - 6] >= 0:
                    move_board[(x + 8 * y) - 6] = -0.25

        if x < 7:
            if (x + 8 * y) - 15 >= 0:
                if move_board[(x + 8 * y) - 15] == -0.5 or move_board[(x + 8 * y) - 15] >= 0:
                    move_board[(x + 8 * y) - 15] = -0.25
            if (x + 8 * y) + 17 < 63:
                if move_board[(x + 8 * y) + 17] == -0.5 or move_board[(x + 8 * y) + 17] >= 0:
                    move_board[(x + 8 * y) + 17] = -0.25

        if x > 0:
            if (x + 8 * y) - 17 >= 0:
                if move_board[(x + 8 * y) - 17] == -0.5 or move_board[(x + 8 * y) - 17] >= 0:
                    move_board[(x + 8 * y) - 17] = -0.25
            if (x + 8 * y) + 15 < 63:
                if move_board[(x + 8 * y) + 15] == -0.5 or move_board[(x + 8 * y) + 15] >= 0:
                    move_board[(x + 8 * y) + 15] = -0.25

        if x >= 2:
            if (x + 8 * y) + 6 <= 63:
                if move_board[(x + 8 * y) + 6] == -0.5 or move_board[(x + 8 * y) + 6] >= 0:
                    move_board[(x + 8 * y) + 6] = -0.25
            if (x + 8 * y) - 10 > 0:
                if move_board[(x + 8 * y) - 10] == -0.5 or move_board[(x + 8 * y) - 10] >= 0:
                    move_board[(x + 8 * y) - 10] = -0.25

        return move_board


class WhiteKnight(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_knight.png")
        self.rect = self.image.get_rect()
        self.point_value = 320
        self.piece_square_table = [-50,-40,-30,-30,-30,-30,-40,-50,
                                    -40,-20,  0,  0,  0,  0,-20,-40,
                                    -30,  0, 10, 15, 15, 10,  0,-30,
                                    -30,  5, 15, 20, 20, 15,  5,-30,
                                    -30,  0, 15, 20, 20, 15,  0,-30,
                                    -30,  5, 10, 15, 15, 10,  5,-30,
                                    -40,-20,  0,  5,  5,  0,-20,-40,
                                    -50,-40,-30,-30,-30,-30,-40,-50]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        if x < 6:
            if (x + 8 * y) + 10 <= 63:
                if move_board[(x + 8 * y) + 10] == -0.5 or move_board[(x + 8 * y) + 10] <= -1:
                    move_board[(x + 8 * y) + 10] = -0.25
            if (x + 8 * y) - 6 > 0:
                if move_board[(x + 8 * y) - 6] == -0.5 or move_board[(x + 8 * y) - 6] <= -1:
                    move_board[(x + 8 * y) - 6] = -0.25

        if x < 7:
            if (x + 8 * y) - 15 >= 0:
                if move_board[(x + 8 * y) - 15] == -0.5 or move_board[(x + 8 * y) - 15] <= -1:
                    move_board[(x + 8 * y) - 15] = -0.25
            if (x + 8 * y) + 17 < 63:
                if move_board[(x + 8 * y) + 17] == -0.5 or move_board[(x + 8 * y) + 17] <= -1:
                    move_board[(x + 8 * y) + 17] = -0.25

        if x > 0:
            if (x + 8 * y) - 17 >= 0:
                if move_board[(x + 8 * y) - 17] == -0.5 or move_board[(x + 8 * y) - 17] <= -1:
                    move_board[(x + 8 * y) - 17] = -0.25
            if (x + 8 * y) + 15 < 63:
                if move_board[(x + 8 * y) + 15] == -0.5 or move_board[(x + 8 * y) + 15] <= -1:
                    move_board[(x + 8 * y) + 15] = -0.25

        if x >= 2:
            if (x + 8 * y) + 6 <= 63:
                if move_board[(x + 8 * y) + 6] == -0.5 or move_board[(x + 8 * y) + 6] <= -1:
                    move_board[(x + 8 * y) + 6] = -0.25
            if (x + 8 * y) - 10 > 0:
                if move_board[(x + 8 * y) - 10] == -0.5 or move_board[(x + 8 * y) - 10] <= -1:
                    move_board[(x + 8 * y) - 10] = -0.25

        return move_board


class BlackRook(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_rook.png")
        self.rect = self.image.get_rect()
        self.point_value = 500
        self.piece_square_table = [0, 0, 0, 5, 5, 0, 0, 0,
                                   - 5, 0, 0, 0, 0, 0, 0, -5,
                                   -5, 0, 0, 0, 0, 0, 0, -5,
                                   - 5, 0, 0, 0, 0, 0, 0, -5,
                                   -5, 0, 0, 0, 0, 0, 0, -5,
                                   -5, 0, 0, 0, 0, 0, 0, -5,
                                   5, 10, 10, 10, 10, 10, 10, 5,
                                   0, 0, 0, 0, 0, 0, 0, 0]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        for i in range(y):
            if move_board[((x + y * 8) - 8 * (i + 1))] == -0.5:
                move_board[((x + y * 8) - 8 * (i + 1))] = -0.25
            elif move_board[((x + y * 8) - 8 * (i + 1))] >= 0:
                move_board[((x + y * 8) - 8 * (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) - 8 * (i + 1))] <= -1:
                break

        for i in range(7 - x):
            if move_board[((x + y * 8) + (i + 1))] == -0.5:
                move_board[((x + y * 8) + (i + 1))] = -0.25
            elif move_board[((x + y * 8) + (i + 1))] >= 0:
                move_board[((x + y * 8) + (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) + (i + 1))] <= -1:
                break

        for i in range(7 - y):
            if move_board[((x + y * 8) + 8 * (i + 1))] == -0.5:
                move_board[((x + y * 8) + 8 * (i + 1))] = -0.25
            elif move_board[((x + y * 8) + 8 * (i + 1))] >= 0:
                move_board[((x + y * 8) + 8 * (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) + 8 * (i + 1))] <= -1:
                break

        for i in range(x):
            if move_board[((x + y * 8) - (i + 1))] == -0.5:
                move_board[((x + y * 8) - (i + 1))] = -0.25
            elif move_board[((x + y * 8) - (i + 1))] >= 0:
                move_board[((x + y * 8) - (i + 1))] = -0.25
                break
            elif move_board[((x + y * 8) - (i + 1))] <= -1:
                break

        return move_board


class WhiteRook(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_rook.png")
        self.rect = self.image.get_rect()
        self.point_value = 500
        self.piece_square_table =[0,  0,  0,  0,  0,  0,  0,  0,
                                  5, 10, 10, 10, 10, 10, 10,  5,
                                 -5,  0,  0,  0,  0,  0,  0, -5,
                                 -5,  0,  0,  0,  0,  0,  0, -5,
                                 -5,  0,  0,  0,  0,  0,  0, -5,
                                 -5,  0,  0,  0,  0,  0,  0, -5,
                                 -5,  0,  0,  0,  0,  0,  0, -5,
                                  0,  0,  0,  5,  5,  0,  0,  0]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        for i in range(y):
            if move_board[((x + y * 8) - 8 * (i+1))] == -0.5:
                move_board[((x + y * 8) - 8 * (i+1))] = -0.25
            elif move_board[((x + y * 8) - 8 * (i+1))] <= -1:
                move_board[((x + y * 8) - 8 * (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) - 8 * (i+1))] >= 0:
                break

        for i in range(7 - x):
            if move_board[((x + y * 8) + (i+1))] == -0.5:
                move_board[((x + y * 8) + (i+1))] = -0.25
            elif move_board[((x + y * 8) + (i+1))] <= -1:
                move_board[((x + y * 8) + (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) + (i+1))] >= 0:
                break

        for i in range(7 - y):
            if move_board[((x + y * 8) + 8 * (i+1))] == -0.5:
                move_board[((x + y * 8) + 8 * (i+1))] = -0.25
            elif move_board[((x + y * 8) + 8 * (i+1))] <= -1:
                move_board[((x + y * 8) + 8 * (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) + 8 * (i+1))] >= 0:
                break

        for i in range(x):
            if move_board[((x + y * 8) - (i+1))] == -0.5:
                move_board[((x + y * 8) - (i+1))] = -0.25
            elif move_board[((x + y * 8) - (i+1))] <= -1:
                move_board[((x + y * 8) - (i+1))] = -0.25
                break
            elif move_board[((x + y * 8) - (i+1))] >= 0:
                break

        return move_board


class BlackPawn(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_pawn.png")
        self.rect = self.image.get_rect()
        self.point_value = 100
        self.moved_two = False
        self.piece_square_table = [ 0,  0,  0,  0,  0,  0,  0,  0,
                                    5, 10, 10, -20, -20, 10, 10, 5,
                                    5, -5, -10, 0, 0, -10, -5, 5,
                                    0, 0, 0, 20, 20, 0, 0, 0,
                                    5, 5, 10, 25, 25, 10, 5, 5,
                                    10, 10, 20, 30, 30, 20, 10, 10,
                                    50, 50, 50, 50, 50, 50, 50, 50,
                                     0,  0,  0,  0,  0,  0,  0,  0]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        if (x+y*8)+8 < 64:
            if move_board[(x+y*8)+8] == -0.5:
                move_board[(x + y * 8)+8] = -0.25
                if y == 1 and move_board[(x+y*8)+16] == -0.5:
                    move_board[(x + y * 8) + 16] = -0.25
            if (x+y*8)+9 < 64:
                if move_board[(x+y*8)+9] >= 0 and x != 7:
                    move_board[(x + y * 8) + 9] = -0.25
            if move_board[(x+y*8)-1] >= 0:
                if isinstance(existing_pieces[move_board[(x+y*8)-1]], WhitePawn):
                    if existing_pieces[move_board[(x+y*8)-1]].moved_two:
                        move_board[(x + y * 8) + 7] = -0.25
            if move_board[(x+y*8)+1] >= 0:
                if isinstance(existing_pieces[move_board[(x+y*8)+1]], WhitePawn):
                    if existing_pieces[move_board[(x+y*8)+1]].moved_two:
                        move_board[(x + y * 8) + 9] = -0.25
            if move_board[(x+y*8)+7] >= 0 and x != 0:
                move_board[(x + y * 8) + 7] = -0.25

        return move_board


class WhitePawn(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_pawn.png")
        self.rect = self.image.get_rect()
        self.point_value = 100
        self.moved_two = False
        self.piece_square_table = [ 0,  0,  0,  0,  0,  0,  0,  0,
                                    50, 50, 50, 50, 50, 50, 50, 50,
                                    10, 10, 20, 30, 30, 20, 10, 10,
                                     5,  5, 10, 25, 25, 10,  5,  5,
                                     0,  0,  0, 20, 20,  0,  0,  0,
                                     5, -5,-10,  0,  0,-10, -5,  5,
                                     5, 10, 10,-20,-20, 10, 10,  5,
                                     0,  0,  0,  0,  0,  0,  0,  0]

    def possible_moves(self, board, existing_pieces):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        if (x + y * 8) - 8 >= 0:
            if move_board[(x+y*8)-8] == -0.5:
                move_board[(x + y * 8)-8] = -0.25
                if y == 6 and move_board[(x+y*8)-16] == -0.5:
                    move_board[(x + y * 8) - 16] = -0.25
            if move_board[(x+y*8)-9] <= -1 and x != 0:
                move_board[(x + y * 8) - 9] = -0.25
            if move_board[(x+y*8)-1] <= -1:
                if isinstance(existing_pieces[move_board[(x+y*8)-1]], BlackPawn):
                    if existing_pieces[move_board[(x+y*8)-1]].moved_two:
                        move_board[(x + y * 8) - 9] = -0.25
            if move_board[(x+y*8)+1] <= -1:
                if isinstance(existing_pieces[move_board[(x+y*8)+1]], BlackPawn):
                    if existing_pieces[move_board[(x+y*8)+1]].moved_two:
                        move_board[(x + y * 8) - 7] = -0.25
            if move_board[(x+y*8)-7] <= -1 and x != 7:
                move_board[(x + y * 8) - 7] = -0.25


        return move_board