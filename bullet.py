import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Classe para gerenciar balas disparadas pela nave'''

    def __init__(self, ai_game):
        '''Cria uma bala na posição atual da nave'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria o rect da bala em (0,0)
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # Coloca na localização certa na tela
        self.rect.midtop = ai_game.spaceship.rect.midtop

        # Armazena a posição da bala com um valor decimal
        self.y = float(self.rect.y)

    def update(self):
        '''Move a bala para cima na tela'''

        # Atualiza a posição da bala
        self.y -= self.settings.bullet_speed

        # Atualiza a posição do rect da bala
        self.rect.y = self.y

    def draw_bullet(self):
        '''Desenha a bala na tela'''
        pygame.draw.rect(self.screen, self.color, self.rect)
