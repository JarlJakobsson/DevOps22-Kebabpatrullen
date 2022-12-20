import random

from utils import visuals


class Character:
    """ Character class, creates a character """

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

    def roll_dice(self):
        """ This method is used to roll a dice """
        return random.randint(1, 6)

    def wait_input(self):  # pragma: no cover
        """ This method is used to wait for user input """
        input("\nPress any key...\n")

    def roll(self, value):
        """ This method is used to roll a dice for a given value """
        sum = 0
        for i in range(value):
            sum += self.roll_dice()
        print(f"{self.name}I try something! (Rolled {sum})")
        print(f"{self.name}: I try something! (Rolled {sum})")
        return sum

    def attack_roll(self):
        """ This method is used to roll a dice for each attack_value of character """
        self.atk_value = 0
        for i in range(self.attack):
            self.atk_value += self.roll_dice()
        print(f"\n{self.name} Tries to attack! ({self.atk_value} attack roll)")
        return self.atk_value

    def initative_roll(self):
        """ This method is used to roll a dice for each initative_value of character """
        initative = 0
        for i in range(self.initiative):
            initative += self.roll_dice()
        print(f"{self.name} tries to take initiative ({initative} initiative roll)")
        return initative

    def dodge_roll(self):
        """ This method is used to roll a dice for each dodge_value of character """
        dodge = 0
        for i in range(self.agility):
            dodge += self.roll_dice()
        print(f"{self.name} tries to dodge ({dodge} dodge roll)")
        return dodge

    def death(self):
        """ This method is used to kill a character """
        self.is_alive = False
        print(f"\n*** {self.name} died... ***\n")
        self.wait_input()
        visuals.clear()

    def take_dmg(self, rogue=0):
        """ This method is used to take damage """
        print(f"\n{self.name}: Ouch!")
        self.health -= (1 + rogue)
        if self.health <= 0:
            self.death()
        else:
            print(f"\n*** {self.name} have {self.health} HP remaining. ***")

    def heal(self):
        """ This method is used to heal a character or monster """
        self.health = self.max_health

    def __repr__(self):
        """ This method is used to represent the object as a string"""
        return self.name
