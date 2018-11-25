import pygame

class white_king(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/white_king.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_x_and_y(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y