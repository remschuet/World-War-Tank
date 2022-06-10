from object import Object
from collision import Collision


class Player(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float, collision):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed, collision)

        self.direction = None

    def move_left(self):
        self.direction = "left"
        if self.collision.next_position(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                        self.direction, self.speed):
            self.position_x -= self.speed
            self.name_image = "tank_left"
            self.set_new_position()

    def move_right(self):
        self.direction = "right"
        if self.collision.next_position(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                        self.direction, self.speed):
            self.position_x += self.speed
            self.name_image = "tank_right"
            self.set_new_position()

    def move_down(self):
        self.direction = "down"
        if self.collision.next_position(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                        self.direction, self.speed):
            self.position_y += self.speed
            self.name_image = "tank_down"
            self.set_new_position()

    def move_up(self):
        self.direction = "up"
        if self.collision.next_position(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                        self.direction, self.speed):
            self.position_y -= self.speed
            self.name_image = "tank_up"
            self.set_new_position()
