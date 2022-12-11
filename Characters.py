import random


class Character:
    # Initiates character attributes
    def __init__(self) -> None:
        self.is_alive = True
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.agility = 0
        self.name = ""
        self.max_health = 0

    # Method to roll 6 sided dice
    def roll_dice(self):
        return random.randint(1, 6)

    # Generic method for all roll mechanics (not used atm)
    def roll(self, value):
        sum = 0
        for i in range(value):
            sum += self.roll_dice()
        print(f"{self.name}I try something! (Rolled {sum})")
        print(f"{self.name}: I try something! (Rolled {sum})")
        return sum

    # Rolls a dice for each attack_value of character
    def attack_roll(self):
        attack = 0
        for i in range(self.attack):
            attack += self.roll_dice()
        print(f"{self.name}I try attack! ({attack} attack roll")
        print(f"{self.name}: I try attack! ({attack} attack roll")
        return attack

    def initative_roll(self):
        initative = 0
        for i in range(self.initiative):
            initative += self.roll_dice()
        print(f"{self.name}I try initiate! ({initative} initiative roll")
        return initative

    def death(self):
        self.is_alive = False
        print("I died!")

        print(f"{self.name}: I try initiate! ({initative} initative roll)")
        return initative

    def dodge_roll(self):
        dodge = 0
        for i in range(self.agility):
            dodge += self.roll_dice()
        print(f"{self.name}I try dodge! ({dodge} dodge roll")
        print(f"{self.name}: I try dodge! ({dodge} dodge roll")
        return dodge

    def death(self):
        self.is_alive = False
        print(f"{self.name}: im death gg")

    # Method to take damage
    def take_dmg(self):
        self.health -= 1
        if self.health == 0:
            self.death()

    # Method to heal monsters if player escapes or if player loads a character
    def heal(self):
        self.health = self.max_health
