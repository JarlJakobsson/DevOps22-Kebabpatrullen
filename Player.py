from random import randint
from BattleMenu import Battle_menu

from Characters import Character


class Player(Character):
    def __init__(self, name="Kebabhunter"):
        super().__init__()
        self.treasure_value = 0
        self.name = name
        self.exits = False
        self.battle_menu = Battle_menu()

    def get_treasure(self, treasure):
        if treasure == 2:
            print(f"{self.name}: I found some gold coins...")
        elif treasure == 6:
            print(f"{self.name}: Sweet! I found a Pouch of gold coins...")
        elif treasure == 10:
            print(f"{self.name}: Cool! I found some Golden Jewlery...")
        elif treasure == 14:
            print(f"{self.name}: Nice! I found a rare Gem")
        elif treasure == 20:
            print(f"{self.name}: WOW! I found a Treasure!")
        else:
            print(f"{self.name}: ...Nothing in here...")

        self.treasure_value += treasure
        print(
            f"\n{self.name}: I have collected {self.treasure_value} worth of treasures."
        )

    def set_position(self, position):
        self.current_position = position

    def escape_roll(self):
        if randint(1, 100) <= 10 * self.agility:
            print("I escaped...")
            return True
        else:
            print("Never lucky...")
            return False

    def attack_roll(self):  ##### FIX BATTLE MENU:
            attack = 0
            for i in range(self.attack):
                attack += self.roll_dice()
            print(f"{self.name}: I try attack! ({attack} attack roll)")
            return attack

    def move(self):
        pass
