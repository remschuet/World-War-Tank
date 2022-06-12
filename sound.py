import pygame
import pygame.mixer


class Sound:
    def __init__(self):
        self.player_left_win = pygame.mixer.Sound("asset/sound/player_left_win.wav")
        self.player_right_win = pygame.mixer.Sound("asset/sound/player_right_win.wav")
        self.bullet_shoot = pygame.mixer.Sound("asset/sound/shoot_bullet.wav")
        self.explosion = pygame.mixer.Sound("asset/sound/collision_bullet.wav")
        self.reload = pygame.mixer.Sound("asset/sound/reload.wav")

    def play_player_left_win(self):
        self.player_left_win.play()

    def play_player_right_win(self):
        self.player_right_win.play()

    def play_bullet_shoot(self):
        self.bullet_shoot.play()

    def play_explosion(self):
        self.explosion.play()

    def play_reload(self):
        self.reload.play()