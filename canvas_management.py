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

        # writing style
        self.arial_font = pygame.font.SysFont("arial", 25, True)

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
            # verify player alive
            self.verify_player_alive()
        elif self.root_menu:
            self.check_key_event_menu()
            self.menu.call_every_frame()

    def verify_player_alive(self):
        if self.gameplay.get_player1_pv() <= 0:
            self.start_menu()

        elif self.gameplay.get_player2_pv() <= 0:
            self.start_menu()

    def start_menu(self):
        self.root_gameplay = False
        self.root_menu = True
        self.create_management_menu()

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
            if event.type == pygame.USEREVENT:
                self.time_secs += 1
                self.gameplay.call_every_seconde()
                print(self.time_secs)
            # key up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    self.gameplay.key_press_shoot("player1")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_v:
                    self.gameplay.key_press_shoot("player2")

        # player mouvement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            self.gameplay.key_pressed_player_1(keys_pressed)
            self.gameplay.key_pressed_player_2(keys_pressed)


    #
    #         self.winner = "right"
    #         self.print_winner()
    #     return self.collision.get_player2_pv()
    #
    # def print_winner(self):
    #     player1_died = self.arial_font.render(f"{self.winner}, win", True, (0, 0, 0))
    #     self.root.blit(player1_died, [120, 20])
    #     print("print winner")