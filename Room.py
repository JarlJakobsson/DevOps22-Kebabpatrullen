import random

from Monsters import Death, Giantspider, Orc, Skeleton, Troll


class Room:
    """ Room class, creates a room with a monster and treasure """

    def __init__(self):
        self.monster = 0
        self.treasure = 0
        self.name = "X"
        self.have_exit = False
        self.have_secret = False
        self.summon_monster()
        self.create_treasure()

    def summon_monster(self):
        """ This method is used to summon a monster """
        monster_roll = random.randint(1, 100)
        if monster_roll in range(1, 20):
            self.monster = Giantspider()
        elif monster_roll in range(21, 36):
            self.monster = Skeleton()
        elif monster_roll in range(37, 47):
            self.monster = Orc()
        elif monster_roll in range(48, 53):
            self.monster = Troll()
        elif monster_roll == 100:
            self.monster = Death()

    def create_treasure(self):
        """ This method is used to create treasure """
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

    def __repr__(self):
        """ This method is used to print the room """
        return self.name
