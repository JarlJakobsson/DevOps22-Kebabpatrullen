import random
from utils import visuals


class Character:
    # Initiates character attributes
    def __init__(self) -> None:
        self.is_alive = True
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.agility = 0
        self.max_health = 0
        self.name = ""
        self.role = ""
        self.ascii = ""

    # Method to roll 6 sided dice
    def roll_dice(self):
        return random.randint(1, 6)

    def wait_input(self):
        input("\nPress Enter...\n")

    # Rolls a dice for each attack_value of character
    def attack_roll(self):
        self.atk_value = 0
        for i in range(self.attack):
            self.atk_value += self.roll_dice()
        print(f"\n{self.name} Tries to attack! ({self.atk_value} attack roll)")
        return self.atk_value

    def initative_roll(self):
        initative = 0
        for i in range(self.initiative):
            initative += self.roll_dice()
        print(f"{self.name} tries to take initiative ({initative} initiative roll)")
        return initative

    def dodge_roll(self):
        dodge = 0
        for i in range(self.agility):
            dodge += self.roll_dice()
        print(f"{self.name} tries to dodge ({dodge} dodge roll)")
        return dodge

    def death(self):
        self.is_alive = False
        print(f"\n*** {self.name} died... ***\n")
        self.wait_input()
        visuals.clear()

    # Method to take damage
    def take_dmg(self, rogue=0):
        print(f"\n{self.name}: Ouch!")
        self.health -= 1 + rogue
        if self.health <= 0:
            self.death()
        else:
            print(f"\n*** {self.name} have {self.health} HP remaining. ***")

    # Method to heal monsters if player escapes or if player loads a character
    def heal(self):
        self.health = self.max_health

    # Method to represent the object as self.name
    def __repr__(self):
        return self.name
