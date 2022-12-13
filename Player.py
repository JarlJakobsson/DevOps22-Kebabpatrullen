from random import randint

from Characters import Character


class Player(Character):
    def __init__(self, name="Kebabhunter"):
        super().__init__()
        self.treasure_value = 0
        self.name = name

    def get_treasure(self, treasure):
        if treasure == 2:
            print(f"{self.name}: I found some gold coins...")
        elif treasure == 6:
            print(f"{self.name}: Sweet! I found a Pouch of gold coins...")
        elif treasure == 10:
            print(f"{self.name}: Cool! I found some Golden Jewlery...")

        self.treasure_value += treasure

    def set_position(self, position):
        self.current_position = position

    def escape_roll(self):
        escape = randint(1, 100)
        if escape <= 10 * self.agility:
            print("I escaped...")
            return True
        else:
            print("Never lucky...")
            return False

    def move(self):
        pass
