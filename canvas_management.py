import pygame
from gameplay import Gameplay
from menu import Menu


class CanvasManagement:
    def __init__(self, root, clock, launched: bool, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.root = root
        self.clock = clock
        self.launched = launched
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        # call every seconde
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # canvas, init to gameplay
        self.root_menu = True
        self.menu = None
        self.root_gameplay = False
        self.gameplay = None

        # create management gameplay
        self.create_management_menu()

        # timer
        self.time_secs = 0

    def create_management_menu(self):
        self.menu = Menu(self.root, self.ROOT_WIDTH, self.ROOT_HEIGHT)

    def create_management_gameplay(self):
        self.gameplay = Gameplay(self.root, self.ROOT_WIDTH, self.ROOT_HEIGHT)

    def get_launched(self):
        return self.launched

    def call_every_frame(self):
        if self.root_gameplay:
            self.gameplay.set_time_secs(self.time_secs)
            self.check_key_event_gameplay()
            self.gameplay.call_every_frame()
        elif self.root_menu:
            self.check_key_event_menu()
            self.menu.call_every_frame()

    def check_key_event_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.launched = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.root_menu = False
                    self.root_gameplay = True
                    self.create_management_gameplay()

    def check_key_event_gameplay(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False
            # create enemy with clock timer
            elif event.type == pygame.USEREVENT:
                self.time_secs += 1
                print(self.time_secs)
            # key up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_3:
                    self.gameplay.key_press_shoot()

        # player mouvement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            self.gameplay.key_pressed(keys_pressed)
