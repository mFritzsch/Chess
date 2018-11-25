import pygame


class WhiteKing(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_king.png")
        self.rect = self.image.get_rect()

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class WhiteQueen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_queen.png")
        self.rect = self.image.get_rect()

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class WhiteBishop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_bishop.png")
        self.rect = self.image.get_rect()

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class WhiteKnight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_knight.png")
        self.rect = self.image.get_rect()

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class WhiteRook(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_rook.png")
        self.rect = self.image.get_rect()

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class WhitePawn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_pawn.png")
        self.rect = self.image.get_rect()

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y