class Settings():
    '''Uma classe para armazenar todas as configurações do jogo Alien Invasion'''

    def __init__(self):
        '''Inicializa as configurações estáticas do jogo'''
        # FPS do jogo
        self.FPS = 60

        # Configurações da tela
        self.WIDTH = 840
        self.HEIGHT = 680
        self.bg_color = (135, 206, 235)

        # Configurações da nave
        self.spaceship_max_lives = 3

        # Configurações das balas
        self.bullet_width = 720
        self.bullet_height = 15
        self.bullet_color = (255, 130, 0)
        self.bullet_allowed = 10

        # Configurações dos aliens
        self.fleet_drop_speed = 10

    def easy_mode_dynamic_settings(self):
        '''Inicializa configurações que mudam durante o jogo no modo fácil'''
        # Velocidade que o jogo vai aumentando a cada frota destruída
        self.game_speedup = 1.1
        self.spaceship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 2.0
        print('Modo fácil')
        self.alien_points = 50
        self.score_scale = 1.5

        # fleet_direction de 1 é a direção que a frota está indo sendo 1 para a direita e -1 para a esquerda
        self.fleet_direction = 1

    def normal_mode_dynamic_settings(self):
        '''Inicializa configurações que mudam durante o jogo no modo normal'''
        self.game_speedup = 2
        self.spaceship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 2.0
        print('Modo normal')
        self.alien_points = 50
        self.score_scale = 3

        # fleet_direction de 1 é a direção que a frota está indo sendo 1 para a direita e -1 para a esquerda
        self.fleet_direction = 1

    def hard_mode_dynamic_settings(self):
        '''Inicializa configurações que mudam durante o jogo no modo difícil'''
        self.game_speedup = 30
        self.spaceship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 2.0
        print('Modo dificil')
        self.alien_points = 50
        self.score_scale = 1000

        # fleet_direction de 1 é a direção que a frota está indo sendo 1 para a direita e -1 para a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        '''Aumenta a velocidade de certos elementos do jogo e a pontuação que cada alien vale'''
        self.spaceship_speed *= self.game_speedup
        self.alien_speed *= self.game_speedup
        self.bullet_speed *= self.game_speedup

        self.alien_points = int(self.alien_points * self.score_scale)
