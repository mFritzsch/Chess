import pygame


class AnyPiece(pygame.sprite.Sprite):
    def __init__(self):
        self.selected = False

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class White(AnyPiece):
    def __init__(self):
        AnyPiece.__init__(AnyPiece)
        self.colour = "white"


class Black(AnyPiece):
    def __init__(self):
        AnyPiece.__init__(AnyPiece)
        self.colour = "black"


class BlackKing(Black):
    def __init__(self):
        Black.__init__(Black)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_king.png")
        self.rect = self.image.get_rect()


class WhiteKing(White):
    def __init__(self):
        White.__init__(White)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_king.png")
        self.rect = self.image.get_rect()


class BlackQueen(Black):
    def __init__(self):
        Black.__init__(Black)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_queen.png")
        self.rect = self.image.get_rect()


class WhiteQueen(White):
    def __init__(self):
        White.__init__(White)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_queen.png")
        self.rect = self.image.get_rect()


class BlackBishop(Black):
    def __init__(self):
        Black.__init__(Black)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_bishop.png")
        self.rect = self.image.get_rect()


class WhiteBishop(White):
    def __init__(self):
        White.__init__(White)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_bishop.png")
        self.rect = self.image.get_rect()


class BlackKnight(Black):
    def __init__(self):
        Black.__init__(Black)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_knight.png")
        self.rect = self.image.get_rect()


class WhiteKnight(White):
    def __init__(self):
        White.__init__(White)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_knight.png")
        self.rect = self.image.get_rect()


class BlackRook(Black):
    def __init__(self):
        Black.__init__(Black)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_rook.png")
        self.rect = self.image.get_rect()


class WhiteRook(White):
    def __init__(self):
        White.__init__(White)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_rook.png")
        self.rect = self.image.get_rect()

    def possible_moves(self, move_board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        i = 1
        if (x + i + y * 8) < 64:
            while move_board[x + i + y * 8] == -1:
                if (x + i + y * 8) < 64:
                    move_board[x + i + y * 8] = -2
                    if ((x + i + y * 8) + 1) % 8 == 0:
                        break
                    i += 1
                else:
                    break
        i = 1
        if (x - i + y * 8) > 0:
            while move_board[x - i + y * 8] == -1:
                if (x - i + y * 8) > -1:
                    move_board[x - i + y * 8] = -2
                    if (x - i + y * 8) % 8 == 0:
                        break
                    i += 1
                else:
                    break
        i = 1
        if (x + (y + i) * 8) < 64:
            while move_board[x + (y + i) * 8] == -1:
                if (x + i + (y - i) * 8) < 64:
                    move_board[x + (y + i) * 8] = -2
                    i += 1
                else:
                    break
        i = 1
        if (x + (y - i) * 8) > 0:
            while move_board[x + (y - i) * 8] == -1:
                if (x + (y - i) * 8) > -1:
                    move_board[x + (y - i) * 8] = -2
                    i += 1
                else:
                    break
        return move_board


class BlackPawn(Black):
    def __init__(self):
        Black.__init__(Black)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/black_pawn.png")
        self.rect = self.image.get_rect()

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        if (x+y*8)+8 < 64:
            if move_board[(x+y*8)+8] == 0:
                move_board[(x + y * 8)+8] = 1
                if y == 1 and move_board[(x+y*8)+16] == 0:
                    move_board[(x + y * 8) + 16] = 1

            if move_board[(x+y*8)+9] > 1:
                move_board[(x + y * 8) + 9] = 1

            if move_board[(x+y*8)+7] > 1:
                move_board[(x + y * 8) + 7] = 1


        return move_board


class WhitePawn(White):
    def __init__(self):
        White.__init__(White)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_pawn.png")
        self.rect = self.image.get_rect()

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        move_board = board[:]
        if (x + y * 8) + 8 < 64:
            if move_board[(x+y*8)-8] == 0:
                move_board[(x + y * 8)-8] = 1
                if y == 6 and move_board[(x+y*8)-16] == 0:
                    move_board[(x + y * 8) - 16] = 1

            if move_board[(x+y*8)-9] < -1:
                move_board[(x + y * 8) - 9] = 1

            if move_board[(x+y*8)-7] < -1:
                move_board[(x + y * 8) - 7] = 1


        return move_board

