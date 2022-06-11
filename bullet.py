from object import Object


class Bullet(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float, collision, direction: str, creation_time: int):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed, collision)

        self.speed = 4

        self.direction = direction
        self.creation_time = creation_time
        self.set_new_position()

    def get_name_id(self):
        return self.name_id

    def get_position(self):
        return self.position_x, self.position_y

    def get_creation_time(self):
        return self.creation_time

    def get_if_check_collision(self):
        return self.collision.check_collision(self.name_id, self.position_x, self.position_y, self.width, self.height)

    def get_if_in_screen(self):
        return self.collision.check_if_in_screen(self.position_x, self.position_y, self.width, self.height)

    def movement(self):
        # move from the player position x, y
        if self.direction == "tank_left":
            self.position_x = self.position_x - self.speed
        if self.direction == "tank_right":
            self.position_x = self.position_x + self.speed
        if self.direction == "tank_up":
            self.position_y = self.position_y - self.speed
        if self.direction == "tank_down":
            self.position_y = self.position_y + self.speed
        # set the new position
        self.set_new_position()
