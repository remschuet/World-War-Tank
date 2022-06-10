from player import Player
import pygame
from collision import Collision
from brick import Brick
from bullet import Bullet


class Gameplay:
    def __init__(self, root, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.root = root
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        self.player = None
        self.time_secs = 0

        self.object_speed = 1.5

        # player
        self.TANK_HEIGHT = 70
        self.TANK_WIDTH = 70

        # image background
        self.gameplay_image_level1 = pygame.image.load("asset/image/background.png")
        self.gameplay_image_level1 = pygame.transform.scale(self.gameplay_image_level1,
                                                            (self.ROOT_WIDTH, self.ROOT_HEIGHT))
        # create collision management
        self.collision = Collision(self.ROOT_WIDTH, self.ROOT_HEIGHT)

        # brick
        self.list_of_brick = []
        self.number_of_brick = 0

        # bullet
        self.list_of_bullet = []
        self.list_of_bullet_to_destroy = []
        self.number_of_bullet = 0
        self.bullet_dimension = 10

        # create player
        self.list_of_player = []
        self.set_new_player()
        self.create_brick_level1()

    def set_time_secs(self, time):
        self.time_secs = time

    def set_new_player(self):
        self.player = Player(self.root, "tank_up", "tank1", 100, 100, self.TANK_WIDTH, self.TANK_HEIGHT,
                             self.object_speed, self.collision)

    def get_time_secs(self):
        return self.time_secs

    def call_every_frame(self):
        # draw background
        self.background_draw()
        # draw object
        self.player.set_object_image()
        self.draw_brick()
        self.draw_bullet()
        # move bullet
        self.move_bullet()

# init and create
    def create_brick_level1(self):
        self.number_of_brick += 1
        self.list_of_brick.append(
            Brick(self.root, "brick", "brick" + str(self.number_of_brick), 300, 300, self.TANK_WIDTH,
                  self.TANK_HEIGHT, self.object_speed, self.collision))

# key event
    def key_pressed(self, keys):
        if keys[pygame.K_LEFT] and self.player.position_x > 0:
            self.player.move_left()
        elif keys[pygame.K_RIGHT] and self.player.position_x < self.ROOT_WIDTH - self.TANK_WIDTH:
            self.player.move_right()
        elif keys[pygame.K_UP] and self.player.position_y > 0:
            self.player.move_up()
        elif keys[pygame.K_DOWN] and self.player.position_y < self.ROOT_HEIGHT - self.TANK_HEIGHT:
            self.player.move_down()

    def key_press_shoot(self):
        self.create_bullet()

# draw
    def background_draw(self):
        self.root.blit(self.gameplay_image_level1, [0, 0])

    def draw_brick(self):
        for brick in self.list_of_brick:
            brick.draw()

    def draw_bullet(self):
        for bullet in self.list_of_bullet:
            bullet.draw()

# bullet
    def remove_bullet_list(self, ):
        for bullet_item in self.list_of_bullet:
            if isinstance(bullet_item, Bullet):
                for item_name_to_destroy in self.list_of_bullet_to_destroy:
                    if bullet_item.name_id == item_name_to_destroy:
                        self.list_of_bullet.remove(bullet_item)

    def destroy_bullet(self, bullet_name):
        self.remove_bullet_list()
        self.collision.destroy_item_in_dict(bullet_name)

    def move_bullet(self):
        for bullet in self.list_of_bullet:
            if bullet.get_if_check_collision() and bullet.get_if_in_screen():
                # mouvement
                bullet.movement()
            else:
                # add in list the bullet to destroy
                bullet_name_id = bullet.get_name_id()
                self.list_of_bullet_to_destroy.append(bullet_name_id)
                # fonction to destroy the bullet
                self.destroy_bullet(bullet_name_id)

    def where_create_bullet(self, x, y, direction):
        # value for not have collision with player
        value = 1
        if direction == "up":
            x += (self.TANK_WIDTH/2) - (self.bullet_dimension/2)
            y -= self.bullet_dimension + value
        elif direction == "down":
            x += (self.TANK_WIDTH/2) - (self.bullet_dimension/2)
            y += self.TANK_HEIGHT + value
        elif direction == "left":
            y += (self.TANK_HEIGHT/2) - (self.bullet_dimension/2)
            x -= self.bullet_dimension + value
        elif direction == "right":
            x += self.TANK_WIDTH + value
            y += (self.TANK_HEIGHT/2) - (self.bullet_dimension/2)
        return x, y

    def create_bullet(self):
        x, y = self.player.get_position()
        direction = self.player.get_direction()
        creation_time = self.time_secs
        x, y = self.where_create_bullet(x, y, direction)
        self.number_of_bullet += 1
        self.list_of_bullet.append(Bullet(self.root, "bullet", "bullet"+str(self.number_of_bullet), x, y,
                                          self.bullet_dimension, self.bullet_dimension,
                                          self.object_speed, self.collision, direction, creation_time))
