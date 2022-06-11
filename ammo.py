from object import Object


class Ammo(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float, collision):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed, collision)