from PlayerRoles import Knight, Wizard, Thief
from Map import Map
import Room
import random
import Enemies


class Game:
    def __init__(self):
        pass

    def create_map(self):
        self.map = Map(int(input("Enter size: ")))

    def move(self, position):
        move = 1
        self.player.position = position
        self.map.player_position = position

    def create_player(self, position, role):
        if role == 1:
            self.player = Knight(position)
        elif role == 2:
            self.player = Wizard(position)
        elif role == 3:
            self.player = Thief(position)

    def check_room(self, position):
        x, y = position
        if self.map.map[x][y].monster:
            print("Monster in here")
            self.battle(position)

    def battle(self, position):
        x, y = position
        if self.player.initative_roll() >= self.map.map[x][y].monster.initative_roll():
            print("player initative")
        else:
            print("monster initatitve")

    def main(self):
        self.player = Wizard()
        self.map = Map()
        self.map.mark_player_position(self.player.position)
        self.check_room(self.player.position)


x = Game()
x.main()
