from PlayerRoles import Knight, Wizard, Thief
from Map import Map


class Game:
    def __init__(self):
        pass

    def create_map(self):
        self.map = Map(int(input("Enter size: ")))

    def create_player(self, position, role):
        if role == 1:
            self.player = Knight(position)
        elif role == 2:
            self.player = Wizard(position)
        elif role == 3:
            self.player = Thief(position)

    def main(self):
        val = mainmeny()
        valcheck(val) # få in namn och rol och position
        self.create_player(val)
        nytt val size
        sizecheck(size) #size and start
        self.create_map(size and start)
        self.map.mark_player_position(self.player.position)
        self.player.move(input("where do you want to move? "))

