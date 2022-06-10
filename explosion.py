from object import Object


class Explosion(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float, collision, creation_time: int):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed, collision)

        self.creation_time = creation_time

    def get_name_id(self):
        return self.name_id

    def get_creation_time(self):
        return self.creation_time

