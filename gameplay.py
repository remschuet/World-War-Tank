from player import Player
import pygame


class Gameplay:
    def __init__(self, root, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.root = root
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        self.player = None
        self.object_speed = 1.5

        # player
        self.TANK_HEIGHT = 70
        self.TANK_WIDTH = 70

        # create player
        self.set_new_player()

        # image background
        self.gameplay_image_level1 = pygame.image.load("asset/image/background.png")
        self.gameplay_image_level1 = pygame.transform.scale(self.gameplay_image_level1,
                                                            (self.ROOT_WIDTH, self.ROOT_HEIGHT))

    def set_new_player(self):
        self.player = Player(self.root, "tank_up", "tank1", 100, 100, self.TANK_WIDTH, self.TANK_HEIGHT, self.object_speed)

    def call_every_frame(self):
        self.background_draw()
        self.player.set_object_image()

    def key_pressed(self, keys):
        if keys[pygame.K_LEFT] and self.player.position_x > 0:
            self.player.move_left()
        elif keys[pygame.K_RIGHT] and self.player.position_x < self.ROOT_WIDTH - self.TANK_WIDTH:
            self.player.move_right()
        elif keys[pygame.K_UP] and self.player.position_y > 0:
            self.player.move_up()
        elif keys[pygame.K_DOWN] and self.player.position_y < self.ROOT_HEIGHT - self.TANK_HEIGHT:
            self.player.move_down()

    def background_draw(self):
        self.root.blit(self.gameplay_image_level1, [0, 0])
