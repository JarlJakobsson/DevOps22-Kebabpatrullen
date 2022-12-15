import random
from Player import Player


class Knight(Player):
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

    # Knight overrides the take_dmg method, to a block check and unique phrase for taking dmg
    # If block is ready it will change block to false and ignore the first damage
    def take_dmg(self):
        if self.block:
            self.block = False
            print(f"\n*** {self.name}: Easy Block! [KNIGHT SPECIAL] ***\n")
        else:
            print(f"{self.name}: Ouch, my shield is not working...")
            self.health -= 1
            if self.health == 0:
                self.death()
            else:
                print(f"{self.name} have {self.health} HP remaining.")


class Wizard(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.initiative = 6
        self.health = 5
        self.attack = 9
        self.agility = 5
        self.max_health = 5
        self.role = "Wizard"

    # Overrides the normal escape method
    def escape_roll(self):
        wizard_escape = random.randint(1, 100)
        if wizard_escape >= 20:
            print(f"\n*** {self.name}: Abracadabra, EZ escape [MAGE SPECIAL] ***")
            return True
        else:
            print(f"\n*** {self.name}: Abraca....what was that spell again? ***\n")
            return False


class Thief(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.initiative = 7
        self.health = 5
        self.attack = 5
        self.agility = 7
        self.max_health = 5
        self.role = "Thief"

    # Overrides the normal attack method
    def attack_roll(self):
        self.atk_value = 0
        if self.battle_menu.run_menu():
            for i in range(self.attack):
                self.atk_value += self.roll_dice()
            thief_atk = random.randint(1, 100)
            if thief_atk >= 75:
                print(f"*** {self.name}: Haiyyaa [THIEF SPECIAL] ***")
                self.atk_value = self.atk_value * 2
            print(f"{self.name} tries to ({self.atk_value} attack roll)")
            return self.atk_value
        else:
            if self.escape_roll():
                self.atk_value = 0
                return self.atk_value
            else:
                self.atk_value = 1
                print(f"{self.name} failed to escape (0 attack roll)")
                return self.atk_value
