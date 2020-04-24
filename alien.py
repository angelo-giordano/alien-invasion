import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''Classe que representa um único alien da frota'''

    def __init__(self, ai_game):
        '''Inicializa o alien define sua posição inicial'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carrega a imagem do alien e pega seu rect
        self.image = pygame.image.load('data\\images\\alien.png')
        self.rect = self.image.get_rect()

        # Cada novo alien aparece perto do canto superior esquerdo da janela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alien
        self.x = float(self.rect.x)

    def check_edges(self):
        '''Retorna True se o alien está no limite da tela'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        '''Move o alien para a direita ou esquerda'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
