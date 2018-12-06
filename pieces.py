import pygame


class AnyPiece(pygame.sprite.Sprite):
    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class WhiteKing(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_king.png")
        self.rect = self.image.get_rect()


class WhiteQueen(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_queen.png")
        self.rect = self.image.get_rect()


class WhiteBishop(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_bishop.png")
        self.rect = self.image.get_rect()


class WhiteKnight(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_knight.png")
        self.rect = self.image.get_rect()


class WhiteRook(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_rook.png")
        self.rect = self.image.get_rect()

    def possible_moves(self, board):
        x = int((self.rect.x - 25) / 100)
        y = int((self.rect.y - 25) / 100)
        i = 1
        if (x + i + y * 8) < 64:
            while board[x + i + y * 8] == -1:
                if (x + i + y * 8) < 64:
                    board[x + i + y * 8] = -2
                    if ((x + i + y * 8) + 1) % 8 == 0:
                        break
                    i += 1
                else:
                    break
        i = 1
        if (x - i + y * 8) > 0:
            while board[x - i + y * 8] == -1:
                if (x - i + y * 8) > -1:
                    board[x - i + y * 8] = -2
                    if (x - i + y * 8) % 8 == 0:
                        break
                    i += 1
                else:
                    break
        i = 1
        if (x + (y + i) * 8) < 64:
            while board[x + (y + i) * 8] == -1:
                if (x + i + (y - i) * 8) < 64:
                    board[x + (y + i) * 8] = -2
                    i += 1
                else:
                    break
        i = 1
        if (x + (y - i) * 8) > 0:
            while board[x + (y - i) * 8] == -1:
                if (x + (y - i) * 8) > -1:
                    board[x + (y - i) * 8] = -2
                    i += 1
                else:
                    break
        print(board)
        return board


class WhitePawn(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_pawn.png")
        self.rect = self.image.get_rect()
