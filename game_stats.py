import json


class GameStats():
    '''Estatísticas do Alien Invasion'''

    def __init__(self, ai_game):
        '''Inicializa as estatísticas'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_playing = False
        self.high_score = 0
        try:
            with open('high_score.json') as json_file:
                self.high_score = json.load(json_file)
        except FileNotFoundError:
            with open('high_score.json', 'w') as json_file:
                json.dump(self.high_score, json_file)

    def reset_stats(self):
        '''Inicializa as estatísticas que podem mudar durante o jogo'''
        self.spaceship_lives = self.settings.spaceship_max_lives
        self.score = 0
        self.wave = 1
