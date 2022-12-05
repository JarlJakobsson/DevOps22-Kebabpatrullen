from Player import Player
import random


class Knight(Player):
    def __init__(self):
        super().__init__()
        self.initative = 5
        self.endurance = 9
        self.attack = 6
        self.agility = 4
        self.is_knight = True
        self.block_rdy = True


def set_block(self):
    if self.block_rdy == True:
        self.block = False
    else:
        self.block_rdy = False


class Wizard(Player):
    def __init__(self):
        super().__init__()
        self.initative = 6
        self.endurance = 5
        self.attack = 9
        self.agility = 5
        self.is_wizard = True

    def escape_roll(self):
        wizard_escape = random.randint(0, 100)
        if wizard_escape >= 20:
            print("WIZARD: Abracadabra, EZ escape")
            return True
        else:
            print("WIZARD: Abraca....what was that spell again?")
            return False


class Thief(Player):
    def __init__(self):
        super().__init__()
        self.initative = 7
        self.endurance = 5
        self.attack = 5
        self.agility = 7
        self.is_thief = True

    def attack_roll(attack_stat):
        atk_value = random.randint(0, 6) * attack_stat
        thief_atk = random.randint(0, 100)
        if thief_atk >= 75:
            print("THIEF: Haiyyaa")
            atk_value = atk_value * 2
        print(f"THIEF: i try attack ({atk_value} attack roll")
        return atk_value
