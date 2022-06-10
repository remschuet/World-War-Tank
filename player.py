from object import Object


class Player(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed)

    def move_left(self):
        self.position_x -= self.speed
        self.name_image = "tank_left"

    def move_right(self):
        self.position_x += self.speed
        self.name_image = "tank_right"

    def move_down(self):
        self.position_y += self.speed
        self.name_image = "tank_down"

    def move_up(self):
        self.position_y -= self.speed
        self.name_image = "tank_up"
