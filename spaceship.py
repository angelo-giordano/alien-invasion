import pygame
import sys


class Spaceship():
    '''Classe para gerir a nave'''

    def __init__(self, ai_game):
        '''Inicializa a nave e define sua posição inicial'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Rect é um objeto do Pygame para armazenar coordenadas retangulares,
        # o que permite tratar elementos do jogo como retângulos

        # Variável que contém o rect da tela do jogo, o que
        # permite com que a nave seja colocada no local correto da tela
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave
        self.image = pygame.image.load('data\\images\\spaceship.png')

        # Rect da superfície da nave
        self.rect = self.image.get_rect()

        # Define a posição inicial de toda nova nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um valor decimal para a posição horizontal da nave,
        # assim você consegue determinar sua posição com exatidão
        self.x = float(self.rect.x)

    def update(self):
        '''Atualiza a posição da nave baseado no sinalizador de movimento'''
        keys = pygame.key.get_pressed()

        # Fechar o jogo com a tecla Esc
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        # Atualiza o valor x da nave se o rect não ultrapassar o tamanho da tela
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed

        # Atualiza o rect.x da nave
        self.rect.x = self.x

    def draw_ship(self):
        '''Desenha a nave na posição definida por 'self.rect' '''
        self.screen.blit(self.image, self.rect)

    def center_spaceship(self):
        '''Centraliza a nave na tela'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
