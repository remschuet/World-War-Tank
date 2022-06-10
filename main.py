import pygame
from canvas_management import CanvasManagement

"""
    REFACTORING
    deteruire l'item dans la list mtn 
"""

pygame.init()

# init the constant variable
ROOT_WIDTH = 900
ROOT_HEIGHT = 600

# timer_create_enemy = 1000

# create root and the background root
root = pygame.display.set_mode((ROOT_WIDTH, ROOT_HEIGHT))
pygame.display.set_caption("Game")

# create the clock (timer)
clock = pygame.time.Clock()

# root open
launched = True

# create canvas_management
canvas_management = CanvasManagement(root, clock, launched, ROOT_WIDTH, ROOT_HEIGHT)

while launched:
    # verify if root is true
    launched = canvas_management.launched

    # reset the screen to black
    root.fill((0, 0, 0))

    # (fps) speed of the mouvement
    clock.tick(90)

    # call every frame
    canvas_management.call_every_frame()

    # main loop
    pygame.display.update()

pygame.quit()
