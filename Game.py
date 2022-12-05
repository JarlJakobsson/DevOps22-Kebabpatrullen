from PlayerRoles import Knight, Wizard, Thief
from Map import Map


class Game:
    def __init__(self):
        pass

    def create_map(self):
        self.map = Map()

    def create_player(self, position, role):
        if role == 1:
            self.player = Knight(position)
        elif role == 2:
            self.player = Wizard(position)
        elif role == 3:
            self.player = Thief(position)
