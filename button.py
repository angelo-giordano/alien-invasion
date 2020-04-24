import pygame.font


class Button():

    def __init__(self, ai_game, message):
        '''Inicializa os atributos do botão'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        # Dimensões do botão
        self.WIDTH, self.HEIGHT = 200, 50
        self.button_color = (self.settings.bg_color)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Coloca o botão no centro da tela
        self.rect = pygame.Rect(150, 150, self.WIDTH, self.HEIGHT)
        self.rect.center = self.screen_rect.center

        self._message(message)

    def _message(self, message):
        '''Transforma a mensagem passada em uma imagem renderizada e centraliza o texto no botão'''
        self.message_img = self.font.render(
            message, True, self.text_color, self.button_color)
        self.message_img_rect = self.message_img.get_rect()
        self.message_img_rect.center = self.rect.center

    def draw_button(self):
        '''Desenha o botão na tela'''
        # Desenha o rect do botão
        self.screen.fill(self.button_color, self.rect)
        # Desenha o texto em forma de imagem
        self.screen.blit(self.message_img, self.message_img_rect)


class EasyModeButton(Button):
    ''''Classe para desenhar o botão do modo fácil'''

    def __init__(self, ai_game, message):
        super().__init__(ai_game, message)
        self.rect = pygame.Rect(150, 150, self.WIDTH, self.HEIGHT)
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.centery
        self.rect.center = self.center_x, self.center_y
        self.message_img_rect.center = self.rect.center

    def draw_button(self):
        '''Desenha o botão do modo fácil na tela'''
        # Desenha o rect do botão
        self.screen.fill(self.button_color, self.rect)
        # Desenha o texto em forma de imagem
        self.screen.blit(self.message_img, self.message_img_rect)

class NormalModeButton(Button):
    ''''Classe para desenhar o botão do modo fácil'''

    def __init__(self, ai_game, message):
        super().__init__(ai_game, message)
        self.rect = pygame.Rect(150, 150, self.WIDTH, self.HEIGHT)
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.centery + 50
        self.rect.center = self.center_x, self.center_y
        self.message_img_rect.center = self.rect.center

    def draw_button(self):
        '''Desenha o botão do modo fácil na tela'''
        # Desenha o rect do botão
        self.screen.fill(self.button_color, self.rect)
        # Desenha o texto em forma de imagem
        self.screen.blit(self.message_img, self.message_img_rect)

class HardModeButton(Button):
    ''''Classe para desenhar o botão do modo fácil'''

    def __init__(self, ai_game, message):
        super().__init__(ai_game, message)
        self.rect = pygame.Rect(150, 150, self.WIDTH, self.HEIGHT)
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.centery + 100
        self.rect.center = self.center_x, self.center_y
        self.message_img_rect.center = self.rect.center

    def draw_button(self):
        '''Desenha o botão do modo fácil na tela'''
        # Desenha o rect do botão
        self.screen.fill(self.button_color, self.rect)
        # Desenha o texto em forma de imagem
        self.screen.blit(self.message_img, self.message_img_rect)

