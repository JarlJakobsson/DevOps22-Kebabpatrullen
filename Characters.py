import random


class Character:
    def __init__(self) -> None:
        self.is_alive = True
        self.initative = 0
        self.health = 0
        self.attack = 0
        self.agility = 0
        self.name = ""
        self.max_health = 0

    def roll_die(self):
        return random.randint(1, 6)

    # eventuell en generisk roll för allt
    def roll(self, value):
        sum = 0
        for i in range(value):
            sum += self.roll_die()
        print(f"{self.name}I try something! (Rolled {sum})")
        return sum

    def attack_roll(self):
        attack = 0
        for i in range(self.attack):
            attack += self.roll_die()
        print(f"{self.name}I try attack! ({attack} attack roll")
        return attack

    def initative_roll(self):
        initative = 0
        for i in range(self.initative):
            initative += self.roll_die()
        print(f"{self.name}I try initiate! ({initative} initative roll")
        return initative

    def death(self):
        self.is_alive = False
        print("im death gg")

    def dodge_roll(self):
        dodge = 0
        for i in range(self.agility):
            dodge += self.roll_die()
        print(f"{self.name}I try dodge! ({dodge} dodge roll")
        return dodge

    def take_dmg(self):
        self.health -= 1
        if self.health == 0:
            self.death()

    def heal(self):
        self.health = self.max_health
