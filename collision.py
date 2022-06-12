class Collision:
    def __init__(self, ROOT_WIDTH, ROOT_HEIGHT, player1_pv, player2_pv):

        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT
        self.player1_pv = player1_pv
        self.player2_pv = player2_pv

        self.box_ammo_to_destroy = False

        self.name_player_took_ammo = None

        # dictionary for object name: x, y, w, h
        self.object_position_dict = {}

        # for the opponent collision
        self.opponent_object = None

    def get_player1_pv(self):
        return self.player1_pv

    def get_player2_pv(self):
        return self.player2_pv

    def get_if_box_ammo_to_destroy(self):
        return self.box_ammo_to_destroy

    def get_name_player_took_ammo(self):
        return self.name_player_took_ammo

    def set_none_player_name_took_ammo(self):
        self.name_player_took_ammo = None

    def set_none_box_ammo_to_destroy(self):
        self.box_ammo_to_destroy = False

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
                    if self.opponent_object == "tank1":
                        print("player 1 down")
                        self.player1_pv -= 1
                    elif self.opponent_object == "tank2":
                        self.player2_pv -= 1
                        print("player 2 down")

                    elif self.opponent_object == "ammo1":
                        self.check_if_collision_with_player(name_id)

                    return False
        return True

    def check_if_collision_with_player(self, name_id):
        if str(name_id) == "tank1":
            self.name_player_took_ammo = "player1"
            self.box_ammo_to_destroy = True
            self.destroy_item_in_dict(self.opponent_object)
        elif str(name_id) == "tank2":
            self.name_player_took_ammo = "player2"
            self.box_ammo_to_destroy = True
            self.destroy_item_in_dict(self.opponent_object)

    def check_if_in_screen(self, position_x, position_y, width, height):
        # value to can verify if is really destroy
        if position_x + width >= 0 and \
                position_x <= self.ROOT_WIDTH and \
                position_y + height >= 0 and \
                position_y <= self.ROOT_HEIGHT:
            return True
        return False

