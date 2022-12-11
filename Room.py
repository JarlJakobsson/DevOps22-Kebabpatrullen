import random

from Enemies import Giantspider, Orc, Skeleton, Troll


class Room:
    def __init__(self, room_index):
        self.visited = False
        self.monster = 0
        self.room_index = room_index
        self.treasure = 0

    def summon_monster(self):  # pragma: no cover
        if not self.visited:
            monster_roll = random.randint(1, 100)
            if monster_roll in range(1, 20):
                self.monster = Giantspider()
            elif monster_roll in range(21, 36):
                self.monster = Skeleton()
            elif monster_roll in range(37, 47):
                self.monster = Orc()
            elif monster_roll in range(48, 53):
                self.monster = Troll()
            if self.monster:
                print(f"There is a {self.monster.name} in here.")

    def create_treasure(self):  # pragma: no cover
        if not self.visited:
            treasure_roll = random.randint(1, 100)
            if treasure_roll in range(1, 40):
                self.treasure = 2
            elif treasure_roll in range(41, 61):
                self.treasure = 6
            elif treasure_roll in range(62, 77):
                self.treasure = 10
            elif treasure_roll in range(78, 88):
                self.treasure = 14
            elif treasure_roll in range(89, 94):
                self.treasure = 20

    def set_visited(self):
        self.visited = True

    def remove_monster(self):
        self.monster = 0

    def remove_treasure(self):
        self.treasure = 0
