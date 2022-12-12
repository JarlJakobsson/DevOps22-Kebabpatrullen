import random

from Player import Player


class Knight(Player):
    def __init__(self):
        super().__init__()
        self.initiative = 5
        self.health = 9
        self.attack = 6
        self.agility = 4
        self.max_health = 9
        self.role = "Knight"
        self.block = True


def set_block(self):
    if self.block_rdy is True:
        self.block_rdy = False
    else:
        self.block_rdy = False


def take_dmg(self):
    if self.block == True:
        self.block = False
        print(f"\n{self.name}: Easy Block!")
    else:
        self.health -= 1
        if self.health == 0:
            self.death()


class Wizard(Player):
    def __init__(self):
        super().__init__()
        self.initiative = 6
        self.health = 5
        self.attack = 9
        self.agility = 5
        self.max_health = 5
        self.role = "Wizard"

    def escape_roll(self):
        wizard_escape = random.randint(1, 100)
        if wizard_escape >= 20:
            print("WIZARD: Abracadabra, EZ escape")
            return True
        else:
            print("WIZARD: Abraca....what was that spell again?")
            return False


class Thief(Player):
    def __init__(self):
        super().__init__()
        self.initiative = 7
        self.health = 5
        self.attack = 5
        self.agility = 7
        self.max_health = 5
        self.role = "Thief"

    def attack_roll(self):
        attack = 0
        thief_atk = random.randint(1, 100)
        for i in range(self.attack):
            attack += self.roll_dice()
            thief_atk = random.randint(0, 100)
        if thief_atk >= 75:
            print("THIEF: Haiyyaa")
            attack = attack * 2
        print(f"{self.name}: I try attack! ({attack} attack roll")
        return attack
