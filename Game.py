from PlayerRoles import Knight, Wizard, Thief


class Game:
    def __init__(self):
        pass

    def create_dungeoun(self):
        self.map = dungeoun

    def create_player(self, position, role):
        if role == 1:
            self.player = Knight(position)
        elif role == 2:
            self.player = Wizard(position)
        elif role == 3:
            self.player = Thief(position)
