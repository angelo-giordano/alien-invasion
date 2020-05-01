import pygame


class Life(pygame.sprite.Sprite):
    '''Cria a sprite das vidas'''

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data\\images\\life.png')
        pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
