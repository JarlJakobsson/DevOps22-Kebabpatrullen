from Characters import Character
from random import randint
from BattleMenu import Battle_menu


class Player(Character):
    def __init__(self, name="Kebabhunter"):
        super().__init__()
        self.treasure_value = 0
        self.name = name
        self.exits = False
        self.battle_menu = Battle_menu()

    def get_treasure(self, treasure):
        if treasure == 2:
            print(f"{self.name}: I found some gold coins (Value 2).")
        elif treasure == 6:
            print(f"{self.name}: Sweet! I found a Pouch of gold coins (Value 6).")
        elif treasure == 10:
            print(f"{self.name}: Cool! I found some Golden Jewlery (Value 10).")
        elif treasure == 14:
            print(f"{self.name}: Nice! I found a rare Gem (Value 14).")
        elif treasure == 20:
            print(f"{self.name}: WOW! I found a Treasure! (Value 20).")
        else:
            print(f"{self.name}: ...No treasures in here...")

        self.treasure_value += treasure
        if treasure:
            print(
                f"\n{self.name}: I have collected treasures worth {self.treasure_value} kebabs."
            )

    def escape_roll(self):
        if randint(1, 100) <= (10 * self.agility):
            return True
        else:
            print(f"\n*** Never lucky...Escape attempt failed ***\n")
            self.wait_input()
            return False

    def attack_roll(self):
        self.atk_value = 0
        if self.battle_menu.run_menu():
            for i in range(self.attack):
                self.atk_value += self.roll_dice()
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
