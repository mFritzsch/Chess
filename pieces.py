import pygame


class AnyPiece(pygame.sprite.Sprite):
    def __init__(self):
        self.selected = False

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


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

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        for i in range(3):
            for j in range(3):
                if 0 < (x + y * 8 - 9) + i + 8 * j < 64 and 8 > (x-1) + i > -1:
                    if move_board[(x + y * 8 - 9) + i + 8 * j] == -0.5 or move_board[(x + y * 8 - 9) + i + 8 * j] >= 0:
                        move_board[(x + y * 8 - 9) + i + 8 * j] = -0.25
        return move_board


class WhiteKing(White):
    def __init__(self):
        White.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_king.png")
        self.rect = self.image.get_rect()

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        for i in range(3):
            for j in range(3):
                if 0 < (x + y * 8 - 9) + i + 8 * j < 64 and 8 > (x-1) + i > -1:
                    if move_board[(x + y * 8 - 9) + i + 8 * j] == -0.5 or move_board[(x + y * 8 - 9) + i + 8 * j] <= -1:
                        move_board[(x + y * 8 - 9) + i + 8 * j] = -0.25
        return move_board


class BlackQueen(Black):
    def __init__(self):
        Black.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_queen.png")
        self.rect = self.image.get_rect()

    def possible_moves(self, board):
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

    def possible_moves(self, board):
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

    def possible_moves(self, board):
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

    def possible_moves(self, board):
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

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        if x < 6:
            if (x + 8 * y) + 10 < 63:
                if move_board[(x + 8 * y) + 10] == -0.5 or move_board[(x + 8 * y) + 10] >= 0:
                    move_board[(x + 8 * y) + 10] = -0.25
            if (x + 8 * y) - 6 > 0:
                if move_board[(x + 8 * y) - 6] == -0.5 or move_board[(x + 8 * y) - 6] >= 0:
                    move_board[(x + 8 * y) - 6] = -0.25

        if x < 7:
            if (x + 8 * y) - 15 > 0:
                if move_board[(x + 8 * y) - 15] == -0.5 or move_board[(x + 8 * y) - 15] >= 0:
                    move_board[(x + 8 * y) - 15] = -0.25
            if (x + 8 * y) + 17 < 63:
                if move_board[(x + 8 * y) + 17] == -0.5 or move_board[(x + 8 * y) + 17] >= 0:
                    move_board[(x + 8 * y) + 17] = -0.25


        if x > 0:
            if (x + 8 * y) - 17 > 0:
                if move_board[(x + 8 * y) - 17] == -0.5 or move_board[(x + 8 * y) - 17] >= 0:
                    move_board[(x + 8 * y) - 17] = -0.25
            if (x + 8 * y) + 15 < 63:
                if move_board[(x + 8 * y) + 15] == -0.5 or move_board[(x + 8 * y) + 15] >= 0:
                    move_board[(x + 8 * y) + 15] = -0.25


        if x >= 2:
            if (x + 8 * y) + 6 < 63:
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

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]

        if x < 6:
            if (x + 8 * y) + 10 < 63:
                if move_board[(x + 8 * y) + 10] == -0.5 or move_board[(x + 8 * y) + 10] <= -1:
                    move_board[(x + 8 * y) + 10] = -0.25
            if (x + 8 * y) - 6 > 0:
                if move_board[(x + 8 * y) - 6] == -0.5 or move_board[(x + 8 * y) - 6] <= -1:
                    move_board[(x + 8 * y) - 6] = -0.25

        if x < 7:
            if (x + 8 * y) - 15 > 0:
                if move_board[(x + 8 * y) - 15] == -0.5 or move_board[(x + 8 * y) - 15] <= -1:
                    move_board[(x + 8 * y) - 15] = -0.25
            if (x + 8 * y) + 17 < 63:
                if move_board[(x + 8 * y) + 17] == -0.5 or move_board[(x + 8 * y) + 17] <= -1:
                    move_board[(x + 8 * y) + 17] = -0.25


        if x > 0:
            if (x + 8 * y) - 17 > 0:
                if move_board[(x + 8 * y) - 17] == -0.5 or move_board[(x + 8 * y) - 17] <= -1:
                    move_board[(x + 8 * y) - 17] = -0.25
            if (x + 8 * y) + 15 < 63:
                if move_board[(x + 8 * y) + 15] == -0.5 or move_board[(x + 8 * y) + 15] <= -1:
                    move_board[(x + 8 * y) + 15] = -0.25


        if x >= 2:
            if (x + 8 * y) + 6 < 63:
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

    def possible_moves(self, board):
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

    def possible_moves(self, board):
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
        self.moved_two = False

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        if (x+y*8)+8 < 64:
            if move_board[(x+y*8)+8] == -0.5:
                move_board[(x + y * 8)+8] = -0.25
                if y == 1 and move_board[(x+y*8)+16] == -0.5:
                    move_board[(x + y * 8) + 16] = -0.25

            if move_board[(x+y*8)+9] < 64:
                if move_board[(x+y*8)+9] >= 0 and x != 7:
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
        self.moved_two = False

    def possible_moves(self, board):
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

            if move_board[(x+y*8)-7] <= -1 and x != 7:
                move_board[(x + y * 8) - 7] = -0.25

        return move_board

