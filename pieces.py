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


class WhitePawn(AnyPiece):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_pawn.png")
        self.rect = self.image.get_rect()
