class Collision:
    def __init__(self, ROOT_WIDTH, ROOT_HEIGHT):

        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        # dictionary for object name: x, y, w, h
        self.object_position_dict = {}

        # for the opponent collision
        self.opponent_object = None

    def set_new_position_in_dict(self, name, position_x, position_y, width, height):
        self.object_position_dict[name] = (position_x, position_y, width, height)

    def destroy_item_in_dict(self, name):
        self.object_position_dict.pop(name)
        print(f"destroy in dict ", name)

    def next_position_player(self, name_id, position_x, position_y, width, height, direction, speed):
        if direction == "tank_up":
            position_y -= speed
        elif direction == "tank_down":
            position_y += speed
        elif direction == "tank_left":
            position_x -= speed
        elif direction == "tank_right":
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

    def check_if_in_screen(self, position_x, position_y, width, height):
        # value to can verify if is really destroy
        value = 50
        if position_x + width >= 0 + value and \
                position_x <= self.ROOT_WIDTH - value and \
                position_y + height >= 0 + value and \
                position_y <= self.ROOT_HEIGHT - value:
            return True
        return False
