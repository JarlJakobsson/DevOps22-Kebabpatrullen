import random


class Character:
    def __init__(self) -> None:
        is_alive = self.is_alive
        self.initative = 0
        self.endurance = 0
        self.attack = 0
        self.agility = 0

    def attack_roll(attack_stat):
        attack_value = random.randint(0, 6) * attack_stat
        print(f"i try attack ({attack_value} attack roll")
        return attack_value

    def death(self):
        self.is_alive = False
        print("im death gg")

    def dodge_roll(self, dodge_stat):
        dodge_value = random.randint(0, 6) * dodge_stat
        print(f"i try dodge ({dodge_value} dodge roll)")
        return dodge_value

    def take_dmg(self):
        self.endurance -= 1
