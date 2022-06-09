import pygame

"""
    REFACTORING
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


launched = True
management_canvas = ManagementCanvas(root, clock, launched, ROOT_WIDTH, ROOT_HEIGHT)
management_canvas.create_management_menu_environment()

while launched:
    # reset the screen to black
    root.fill((0, 0, 0))

    # (fps) speed of the mouvement
    clock.tick(120)

    # verify if the game is launch
    launched = management_canvas.launched

    # check the event in management canvas
    management_canvas.call_every_frame()

    # main loop
    pygame.display.update()

pygame.quit()
