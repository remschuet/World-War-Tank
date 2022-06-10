class Collision:
    def __init__(self):
        # dictionary for object name: x, y, w, h
        self.object_position_dict = {}

        # for the opponent collision
        self.opponent_object = None

    def set_new_position_in_dict(self, name, position_x, position_y, width, height):
        self.object_position_dict[name] = (position_x, position_y, width, height)
        # print(self.object_position_dict)

    def next_position(self, name_id, position_x, position_y, width, height, direction, speed):
        if direction == "up":
            position_y -= speed
        elif direction == "down":
            position_y += speed
        elif direction == "left":
            position_x -= speed
        elif direction == "right":
            position_x += speed

        if self.check_collision(name_id, position_x, position_y, width, height):
            return True
        else:
            return False

    def check_collision(self, name_id, position_x, position_y, width, height):
        for self.opponent_object, (x, y, w, h) in self.object_position_dict.items():
            if name_id != self.opponent_object:
                if position_x + width >= x and \
                        position_x <= x + w and \
                        position_y + height >= y and \
                        position_y <= y + h:
                    return False
        return True
