import pygame
import pygame.mixer


class Sound:
    def __init__(self):
        self.player_left_win = pygame.mixer.Sound("asset/sound/player_left_win.wav")
        self.player_right_win = pygame.mixer.Sound("asset/sound/player_right_win.wav")

    def play_player_left_win(self):
        self.player_left_win.play()

    def play_player_right_win(self):
        self.player_right_win.play()

