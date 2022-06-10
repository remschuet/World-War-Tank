import pygame


class Menu:
    def __init__(self, root, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.root = root
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        # image background
        self.gameplay_image_level1 = pygame.image.load("asset/image/background_menu.png")
        self.gameplay_image_level1 = pygame.transform.scale(self.gameplay_image_level1,
                                                            (self.ROOT_WIDTH, self.ROOT_HEIGHT))

    def call_every_frame(self):
        # draw background
        self.background_draw()

    def background_draw(self):
        self.root.blit(self.gameplay_image_level1, [0, 0])


