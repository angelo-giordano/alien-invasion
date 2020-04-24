import sys
from time import sleep
import pygame
from settings import Settings
from spaceship import Spaceship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
import button
from scoreboard import Scoreboard

# Teste

class AlienInvasion():
    '''Classe geral para gerir os componentes e o comportamento do jogo'''

    def __init__(self):
        """Inicializa o jogo e cria os recursos do mesmo"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Carregando a janela do jogo
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))

        pygame.display.set_caption('Alien Invasion')

        self.game_stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.easy_game_button = button.EasyModeButton(self, 'Easy')
        self.normal_game_button = button.NormalModeButton(self, 'Normal')
        self.hard_game_button = button.HardModeButton(self, 'Hard')
        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _check_events(self):
        '''Responde aos inputs de mouse e teclado'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_easy_game_button(mouse_position)
                self._check_normal_game_button(mouse_position)
                self._check_hard_game_button(mouse_position)

        self.spaceship.update()

    def _check_easy_game_button(self, mouse_position):
        '''Começa um novo jogo quando o jogador clica em Start'''
        button_clicked = self.easy_game_button.rect.collidepoint(
            mouse_position)
        if button_clicked and not self.game_stats.game_playing:
            self._start_new_easy_mode_game()

    def _check_normal_game_button(self, mouse_position):
        '''Começa um novo jogo quando o jogador clica em Start'''
        button_clicked = self.normal_game_button.rect.collidepoint(
            mouse_position)
        if button_clicked and not self.game_stats.game_playing:
            self._start_new_normal_mode_game()

    def _check_hard_game_button(self, mouse_position):
        '''Começa um novo jogo quando o jogador clica em Start'''
        button_clicked = self.hard_game_button.rect.collidepoint(
            mouse_position)
        if button_clicked and not self.game_stats.game_playing:
            self._start_new_hard_mode_game()

    def _start_new_easy_mode_game(self):
        '''Cria um novo jogo destruindo os aliens e as balas restantes'''
        self.settings.easy_mode_dynamic_settings()
        self.game_stats.reset_stats()
        self.game_stats.game_playing = True
        self.scoreboard._score()
        self.scoreboard._wave()
        self.scoreboard._lifes()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.spaceship.center_spaceship()

        pygame.mouse.set_visible(False)

    def _start_new_normal_mode_game(self):
        '''Cria um novo jogo destruindo os aliens e as balas restantes'''
        self.settings.normal_mode_dynamic_settings()
        self.game_stats.reset_stats()
        self.game_stats.game_playing = True
        self.scoreboard._score()
        self.scoreboard._wave()
        self.scoreboard._lifes()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.spaceship.center_spaceship()

        pygame.mouse.set_visible(False)

    def _start_new_hard_mode_game(self):
        '''Cria um novo jogo destruindo os aliens e as balas restantes'''
        self.settings.hard_mode_dynamic_settings()
        self.game_stats.reset_stats()
        self.game_stats.game_playing = True
        self.scoreboard._score()
        self.scoreboard._wave()
        self.scoreboard._lifes()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.spaceship.center_spaceship()

        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        '''Cria uma nova bala e a adiciona no grupo bullets
        se o número de balas na tela for menor que o permitido'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        '''Cria uma frota de aliens'''
        # Cria um alien
        alien = Alien(self)
        # Acha o número de aliens que cabem numa linha
        # Pega a largura e a altura de um alien
        alien_width, alien_height = alien.rect.size
        # Calcula o espaço horizontal vazio
        space_x = self.settings.WIDTH - (2 * alien_width)
        # Calcula quantos aliens cabem nesse espaço vazio
        number_aliens_x = space_x // (2 * alien_width)

        # Determina o número de linhas que cabem na tela
        spaceship_height = self.spaceship.rect.height
        space_y = (self.settings.HEIGHT -
                   (3 * alien_height) - spaceship_height)
        number_rows = space_y // (4 * alien_height)

        # Cria uma frota de aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''Cria um alien e o coloca na linha'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Define a coordenada x onde ele vai ser colocado
        alien.x = alien_width + 2 * alien_width * alien_number
        # Define a posição do rect
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        # Adiciona o novo alien para o grupo aliens
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''Responde de acordo se um alien enconstar no limite'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Faz toda a frota descer e muda a direção da mesma'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _spaceship_hit(self):
        '''Ação que ocorre quando a nave é acertada por um alien'''
        # Duminui o número de vidas
        if self.game_stats.spaceship_lives > 0:
            self.game_stats.spaceship_lives -= 1
            self.scoreboard._lifes()

            # Destrói os aliens e as balas restantes
            self.aliens.empty()
            self.bullets.empty()

            # Cria uma nova frota
            self._create_fleet()
            # Centraliza a nave
            self.spaceship.center_spaceship()

            # Pausa
            sleep(0.5)
        else:
            self.game_stats.game_playing = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        '''Atualiza a posição das balas e exclui as que não aparecem mais na tela'''

        # Atualiza a posição das balas
        self.bullets.update()

        # Excluindo as balas que não estão mais aparecendo na tela
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''Colisão entre as balas e os aliens'''

        # Checa por qualquer bala que acertou os aliens, e caso acerte exclui a bala e o alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)

        if collisions:
            for aliens in collisions.values():
                self.game_stats.score += self.settings.alien_points * \
                    len(aliens)
            self.scoreboard._score()
            self.scoreboard.check_highscore()

        if not self.aliens:
            # Destrói balas existentes
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.game_stats.wave += 1
            self.scoreboard._wave()

    def _update_screen(self):
        '''Preenche a tela com as imagens, e muda para um nova janela'''
        self.screen.fill(self.settings.bg_color)
        self.spaceship.draw_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.scoreboard.draw_score()

        if not self.game_stats.game_playing:
            # self.easy_game_button.draw_button()
            self.draw_buttons()

        pygame.display.flip()

    def draw_buttons(self):
        '''Desenha os botôes na tela'''
        self.easy_game_button.draw_button()
        self.normal_game_button.draw_button()
        self.hard_game_button.draw_button()

    def _check_aliens_in_bottom(self):
        '''Verifica se nenhum alien chegou na parte de baixo da tela'''
        screen_rect = self.screen.get_rect()
        # Passa por cada alien no grupo de aliens verificando se encostou no limite de baixo da tela
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._spaceship_hit()
                break

    def _update_aliens(self):
        '''Atualiza a posição de todos os aliens da frota
            após verificar se a frota está no limite da janela'''
        self._check_fleet_edges()
        self.aliens.update()

        # Vê se um alien atingiu a nave, e caso atinja o número de vidas diminui em 1
        if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
            self._spaceship_hit()

        self._check_aliens_in_bottom()

    def run_game(self):
        '''Inicia o loop principal do jogo'''
        while True:
            self.clock.tick(self.settings.FPS)
            self._check_events()
            if self.game_stats.game_playing:
                self.spaceship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == "__main__":
    # Instância o jogo
    alien_invasion = AlienInvasion()
    # Inicia o jogo
    alien_invasion.run_game()
