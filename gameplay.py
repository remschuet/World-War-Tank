from player import Player
import pygame
from collision import Collision
from brick import Brick
from bullet import Bullet
from explosion import Explosion
from sound import Sound
from box_ammo import BoxAmmo


class Gameplay:
    def __init__(self, root, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.root = root
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        self.player1 = None
        self.player1_pv = 3
        self.player2 = None
        self.player2_pv = 3

        self.time_secs = 0

        self.object_speed = 1.5

        # ammo
        self.list_of_box_ammo = []
        self.number_of_box_ammo = 0

        # player
        self.OBJECT_HEIGHT = 70
        self.OBJECT_WIDTH = 70

        # create sound
        self.sound = Sound()

        # image background
        self.gameplay_image_level1 = pygame.image.load("asset/image/background.png")
        self.gameplay_image_level1 = pygame.transform.scale(self.gameplay_image_level1,
                                                            (self.ROOT_WIDTH, self.ROOT_HEIGHT))
        # create collision management
        self.collision = Collision(self.ROOT_WIDTH, self.ROOT_HEIGHT, self.player1_pv, self.player2_pv)

        # brick
        self.list_of_brick = []
        self.number_of_brick = 0

        # bullet
        self.list_of_bullet = []
        self.list_of_bullet_to_destroy = []
        self.number_of_bullet = 0
        self.bullet_dimension = 10

        # ammo
        self.number_of_ammo_player1 = None
        self.number_of_ammo_player2 = None
        self.create_box_ammo()

        # particule
        self.list_of_particule = []
        self.list_of_particule_to_destroy = []
        self.number_of_particule = 0
        self.particule_dimension = 40

        # create player
        self.list_of_player = []
        self.set_new_player()

        # writing style
        self.arial_font = pygame.font.SysFont("arial", 25, True)

        # level 1
        self.create_level1()

    def set_time_secs(self, time):
        self.time_secs = time

    def set_new_player(self):
        self.player1 = Player(self.root, "tank_left", "tank1", self.ROOT_WIDTH - self.OBJECT_WIDTH,
                              int(self.ROOT_HEIGHT/2 - self.OBJECT_HEIGHT/2), self.OBJECT_WIDTH, self.OBJECT_HEIGHT,
                              self.object_speed, self.collision)
        self.player1.set_new_position()

        self.player2 = Player(self.root, "tank_right", "tank2", 0, int(self.ROOT_HEIGHT/2 - self.OBJECT_HEIGHT/2),
                              self.OBJECT_WIDTH, self.OBJECT_HEIGHT, self.object_speed, self.collision)
        self.player2.set_new_position()

    def get_time_secs(self):
        return self.time_secs

    def call_every_seconde(self):
        print()

    def call_every_frame(self):
        # reset background
        self.background_reset()
        # draw object
        self.management_draw()
        # move bullet
        self.move_bullet()
        # particule
        self.management_particule()
        # box_ammo
        self.management_box_ammo()

# init and create
    def create_brick(self, x, y):
        self.number_of_brick += 1
        self.list_of_brick.append(
            Brick(self.root, "brick", "brick" + str(self.number_of_brick), x, y, self.OBJECT_WIDTH,
                  self.OBJECT_HEIGHT, self.object_speed, self.collision))

    def get_player1_pv(self):
        if self.collision.get_player1_pv() <= 0:
            self.sound.play_player_right_win()
        return self.collision.get_player1_pv()

    def get_player2_pv(self):
        if self.collision.get_player2_pv() <= 0:
            self.sound.play_player_left_win()
        return self.collision.get_player2_pv()

# key event
    def key_pressed_player_1(self, keys):
        if keys[pygame.K_LEFT] and self.player1.position_x > 0:
            self.player1.move_left()
        elif keys[pygame.K_RIGHT] and self.player1.position_x < self.ROOT_WIDTH - self.OBJECT_WIDTH:
            self.player1.move_right()
        elif keys[pygame.K_UP] and self.player1.position_y > 0:
            self.player1.move_up()
        elif keys[pygame.K_DOWN] and self.player1.position_y < self.ROOT_HEIGHT - self.OBJECT_HEIGHT:
            self.player1.move_down()

    def key_pressed_player_2(self, keys):
        if keys[pygame.K_a] and self.player2.position_x > 0:
            self.player2.move_left()
        elif keys[pygame.K_d] and self.player2.position_x < self.ROOT_WIDTH - self.OBJECT_WIDTH:
            self.player2.move_right()
        elif keys[pygame.K_w] and self.player2.position_y > 0:
            self.player2.move_up()
        elif keys[pygame.K_s] and self.player2.position_y < self.ROOT_HEIGHT - self.OBJECT_HEIGHT:
            self.player2.move_down()

    def key_press_shoot(self, player: str):
        self.player_name_create_bullet(player)

# draw
    def management_draw(self):
        self.player1.set_object_image()
        self.player2.set_object_image()

        self.draw_brick()
        self.draw_bullet()
        self.draw_box_ammo()
        self.draw_particule()
        self.draw_players_number_ammo()

    def background_reset(self):
        self.root.blit(self.gameplay_image_level1, [0, 0])

    def draw_brick(self):
        for brick in self.list_of_brick:
            brick.draw()

    def draw_box_ammo(self):
        for box_ammo in self.list_of_box_ammo:
            if isinstance(box_ammo, BoxAmmo):
                box_ammo.draw()

    def draw_bullet(self):
        for bullet in self.list_of_bullet:
            bullet.draw()

    def draw_particule(self):
        for particule in self.list_of_particule:
            particule.draw()

    def draw_players_number_ammo(self):
        player1_ammo = self.arial_font.render(f"{self.number_of_ammo_player1} bullets", True, (0, 0, 0))
        self.root.blit(player1_ammo, [(self.ROOT_WIDTH - 110), 20])

        player2_ammo = self.arial_font.render(f"{self.number_of_ammo_player2} bullets", True, (0, 0, 0))
        self.root.blit(player2_ammo, [20, 20])

# bullet
    def remove_bullet_list(self):
        for bullet_item in self.list_of_bullet:
            if isinstance(bullet_item, Bullet):
                for item_name_to_destroy in self.list_of_bullet_to_destroy:
                    if bullet_item.name_id == item_name_to_destroy:
                        # x, y = bullet_item.get_position()
                        self.list_of_bullet.remove(bullet_item)
                        # self.create_particule(x, y)

    def destroy_bullet(self, bullet_name):
        self.remove_bullet_list()
        self.collision.destroy_item_in_dict(bullet_name)

    def move_bullet(self):
        for bullet in self.list_of_bullet:
            if bullet.get_if_check_collision():
                if bullet.get_if_in_screen():
                    # mouvement
                    bullet.movement()
                else:
                    self.bullet_cant_move(bullet)
            else:
                x, y = bullet.get_position()
                self.create_particule(x, y)
                self.bullet_cant_move(bullet)

    def bullet_cant_move(self, bullet):
        # add in list the bullet to destroy
        bullet_name_id = bullet.get_name_id()
        self.list_of_bullet_to_destroy.append(bullet_name_id)
        # fonction to destroy the bullet
        self.destroy_bullet(bullet_name_id)

    def position_for_create_bullet(self, x, y, direction):
        # value for not have collision with player
        value = 1
        if direction == "tank_up":
            x += (self.OBJECT_WIDTH / 2) - (self.bullet_dimension / 2)
            y -= self.bullet_dimension + value
        elif direction == "tank_down":
            x += (self.OBJECT_WIDTH / 2) - (self.bullet_dimension / 2)
            y += self.OBJECT_HEIGHT + value
        elif direction == "tank_left":
            y += (self.OBJECT_HEIGHT / 2) - (self.bullet_dimension / 2)
            x -= self.bullet_dimension + value
        elif direction == "tank_right":
            x += self.OBJECT_WIDTH + value
            y += (self.OBJECT_HEIGHT / 2) - (self.bullet_dimension / 2)
        return x, y

    def player_name_create_bullet(self, player: str):
        if player == "player1":
            if self.number_of_ammo_player1 >= 1:
                self.number_of_ammo_player1 -= 1
                x, y = self.player1.get_position()
                direction = self.player1.get_direction()
                self.create_bullet(x, y, direction)
        # player 2
        else:
            if self.number_of_ammo_player2 >= 1:
                self.number_of_ammo_player2 -= 1
                x, y = self.player2.get_position()
                direction = self.player2.get_direction()
                self.create_bullet(x, y, direction)

    def create_bullet(self, x, y, direction):
        creation_time = self.time_secs
        x, y = self.position_for_create_bullet(x, y, direction)
        self.number_of_bullet += 1
        self.list_of_bullet.append(Bullet(self.root, "bullet", "bullet"+str(self.number_of_bullet), x, y,
                                          self.bullet_dimension, self.bullet_dimension,
                                          self.object_speed, self.collision, direction, creation_time))

# particule
    def management_particule(self):
        self.check_particule_time_creation()
        self.remove_particule_list()

    def create_particule(self, x, y):
        self.number_of_particule += 1
        creation_time = self.time_secs
        self.list_of_particule.append(Explosion(self.root, "explosion", "explosion"+str(self.number_of_particule),
                                                x-20, y-20, self.particule_dimension, self.particule_dimension,
                                                self.object_speed, self.collision, creation_time))

    def check_particule_time_creation(self):
        for particule in self.list_of_particule:
            if isinstance(particule, Explosion):
                time_creation = particule.get_creation_time()
                time_present = self.get_time_secs()
                if time_present - time_creation >= 1:
                    name = particule.get_name_id()
                    self.list_of_particule_to_destroy.append(name)

    def remove_particule_list(self):
        for particule in self.list_of_particule:
            if isinstance(particule, Explosion):
                for particule_to_destroy in self.list_of_particule_to_destroy:
                    if particule.name_id == particule_to_destroy:
                        self.list_of_particule.remove(particule)
                        self.list_of_particule_to_destroy.clear()

# box ammo
    def management_box_ammo(self):
        player_name = self.collision.get_name_player_took_ammo()
        if player_name:
            if player_name == "player1":
                self.number_of_ammo_player1 += 5
            elif player_name == "player2":
                self.number_of_ammo_player2 += 5
            self.collision.set_none_player_name_took_ammo()
            if self.collision.get_if_box_ammo_to_destroy():
                self.destroy_box_ammo()

    def destroy_box_ammo(self):
        self.list_of_box_ammo.clear()
        self.collision.set_none_box_ammo_to_destroy()

    def create_box_ammo(self):
        if not self.list_of_box_ammo:
            self.number_of_box_ammo += 1
            self.list_of_box_ammo.append(BoxAmmo(self.root, "ammo", "ammo1", 430, 270, int(self.OBJECT_WIDTH / 1.5),
                                                 int(self.OBJECT_HEIGHT / 1.5), self.object_speed, self.collision))

# level
    def create_level1(self):
        self.number_of_ammo_player1 = 10
        self.number_of_ammo_player2 = 10

        self.create_brick(700, 50)
        self.create_brick(150, 100)
        self.create_brick(500, 500)

        self.create_brick(450, 100)
        self.create_brick(450, 165)

        self.create_brick(250, 260)
        self.create_brick(250, 325)
        self.create_brick(250, 390)

        self.create_brick(650, 260)
        self.create_brick(650, 325)
        self.create_brick(650, 390)

    def create_level2(self):
        self.number_of_ammo_player1 = 10
        self.number_of_ammo_player2 = 10

        self.create_brick(700, 50)
        self.create_brick(150, 100)
        self.create_brick(500, 500)

        self.create_brick(450, 100)
        self.create_brick(450, 165)

        self.create_brick(250, 260)
        self.create_brick(250, 325)
        self.create_brick(250, 390)

        self.create_brick(650, 260)
        self.create_brick(650, 325)
        self.create_brick(650, 390)