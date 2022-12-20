import random

from Player import Player


class Knight(Player):
    """ Knight class, inherits from Player class """

    def __init__(self):
        super().__init__()
        self.name = ""
        self.initiative = 5
        self.health = 9
        self.attack = 6
        self.agility = 4
        self.max_health = 9
        self.role = "Knight"
        self.block = True

    def take_dmg(self):
        """ Knight takes damage, if block is ready it will ignore the first damage """
        if self.block:
            self.block = False
            print(f"\n*** {self.name}: Easy Block! [KNIGHT SPECIAL] ***\n")
        else:
            print(f"\n{self.name}: Ouch, my shield is not working...\n")
            self.health -= 1
            if self.health == 0:
                self.death()
            else:
                print(f"{self.name} have {self.health} HP remaining.")


class Wizard(Player):
    """ Wizard class, inherits from Player class """

    def __init__(self):
        super().__init__()
        self.name = ""
        self.initiative = 6
        self.health = 5
        self.attack = 9
        self.agility = 5
        self.max_health = 5
        self.role = "Wizard"

    def escape_roll(self):
        """ Wizard tries to escape, if successful it will return True """
        wizard_escape = random.randint(1, 100)
        if wizard_escape >= 20:
            print(f"\n*** {self.name}: Abracadabra, EZ escape [MAGE SPECIAL] ***")
            return True
        else:
            print(f"\n*** {self.name}: Abraca....what was that spell again? ***\n")
            return False


class Thief(Player):
    """ Thief class, inherits from Player class """

    def __init__(self):
        super().__init__()
        self.name = ""
        self.initiative = 7
        self.health = 5
        self.attack = 5
        self.agility = 7
        self.max_health = 5
        self.role = "Thief"

    def attack_roll(self):
        """ Thief tries to attack, if successful it will return the attack value """
        self.atk_value = 0
        self.battle_menu.run_menu()
        if self.battle_menu.choice == 1:
            for i in range(self.attack):
                self.atk_value += self.roll_dice()
            thief_atk = random.randint(1, 100)
            if thief_atk >= 75:
                print(f"*** {self.name}: HAIYAAA!! [THIEF SPECIAL] ***")
                self.atk_value = self.atk_value * 2
            print(f"{self.name} tries to attack({self.atk_value} attack roll)")
            return self.atk_value
        elif not self.battle_menu.choice:
            if self.escape_roll():
                self.atk_value = 0
                return self.atk_value
            else:
                self.atk_value = 1
                return self.atk_value
