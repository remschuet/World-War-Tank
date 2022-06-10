import pygame
from management_gameplay import ManagementGameplay


class CanvasManagement:
    def __init__(self, root, clock, launched: bool, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.root = root
        self.clock = clock
        self.launched = launched
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        # call every x milliseconds
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # canvas, init to gameplay
        self.root_gameplay = True
        self.management_gameplay = None

        # create management gameplay
        self.crete_management_gameplay()

        # timer
        self.time_secs = 0

    def crete_management_gameplay(self):
        self.management_gameplay = ManagementGameplay()

    def get_launched(self):
        return self.launched

    def call_every_frame(self):
        if self.root_gameplay:
            self.check_key_event_gameplay()

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
                    print("key 3 press")

        # player mouvement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            return


