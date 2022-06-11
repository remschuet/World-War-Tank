from object import Object


class Player(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float, collision):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed, collision)

        self.direction = name_image

    def get_position(self):
        return self.position_x, self.position_y

    def get_direction(self):
        return self.direction

    def move_left(self):
        self.name_image = "tank_left"
        self.direction = "tank_left"
        if self.collision.next_position_player(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                               self.direction, self.speed):
            self.position_x -= self.speed
            self.set_new_position()

    def move_right(self):
        self.name_image = "tank_right"
        self.direction = "tank_right"
        if self.collision.next_position_player(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                               self.direction, self.speed):
            self.position_x += self.speed
            self.set_new_position()

    def move_down(self):
        self.name_image = "tank_down"
        self.direction = "tank_down"
        if self.collision.next_position_player(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                               self.direction, self.speed):
            self.position_y += self.speed
            self.set_new_position()

    def move_up(self):
        self.name_image = "tank_up"
        self.direction = "tank_up"
        if self.collision.next_position_player(self.name_id, self.position_x, self.position_y, self.width, self.height,
                                               self.direction, self.speed):
            self.position_y -= self.speed
            self.set_new_position()
