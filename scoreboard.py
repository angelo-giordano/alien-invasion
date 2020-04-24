import pygame.font
from pygame.sprite import Group
from life import Life
import json


class Scoreboard():
    '''Classe para mostrar a pontução do jogador'''

    def __init__(self, ai_game):
        '''Inicializa atributos da pontuação'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        # Configurações de fonte para a pontuação
        self.text_color = (30, 30, 30)

        self._score()
        self._high_score()
        self._wave()
        self._lifes()

    def _score(self):
        '''Transforma a pontuação em uma imagem renderizada'''
        self.font = pygame.font.SysFont(None, 30)
        rounded_score = round(self.game_stats.score, -1)
        score_string = str(f'{rounded_score:,}')
        self.score_image = self.font.render(
            score_string, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20

    def _high_score(self):
        '''Transforma a maior pontuação em uma imagem renderizada'''
        self.font = pygame.font.SysFont(None, 55)
        high_score = round(self.game_stats.high_score, -1)
        high_score_string = str(f'{high_score:,}')
        self.high_score_image = self.font.render(
            high_score_string, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.score_rect.top

    def _wave(self):
        '''Transforma as rodadas que o jogar está em uma imagem renderizada'''
        self.font = pygame.font.SysFont(None, 30)
        wave_string = str(f'Wave {self.game_stats.wave}')
        self.wave_image = self.font.render(
            wave_string, True, self.text_color, self.settings.bg_color)

        self.wave_rect = self.wave_image.get_rect()
        self.wave_rect.right = self.score_rect.right
        self.wave_rect.top = self.score_rect.bottom + 5

    def _lifes(self):
        '''Mostra quantas vidas restam'''
        self.lifes = Group()
        for life_number in range(self.game_stats.spaceship_lives):
            life = Life()
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = self.screen_rect.top
            self.lifes.add(life)

    def draw_score(self):
        '''Desenha a pontuação, a rodada e o número de vidas restantes na tela'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.wave_image, self.wave_rect)
        self.lifes.draw(self.screen)

    def check_highscore(self):
        '''Verifica se tem uma nova pontuação mais alta'''
        if self.game_stats.score > self.game_stats.high_score:
            with open('high_score.json', 'w') as json_file:
                self.game_stats.high_score = self.game_stats.score
                json.dump(self.game_stats.high_score, json_file)
            self._high_score()
