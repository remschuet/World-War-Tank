class Collision:
    def __init__(self):
        # dictionary for object name: x, y, w, h
        self.object_position_dict = {}

        # for the opponent collision
        self.opponent_object = None

    def set_new_position_in_dict(self, name, position_x, position_y, width, height):
        self.object_position_dict[name] = (position_x, position_y, width, height)
        print(self.object_position_dict)
