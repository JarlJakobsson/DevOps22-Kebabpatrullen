from Characters import Character


class Player(Character):
    def __init__(self, position):
        super().__init__()
        self.treasure_value = 0
        self.current_position = position

    def get_treasure(self, treasure):
        self.treasure_value += treasure
        if treasure == 2:
            print("I found some gold coins...")
        elif treasure == 6:
            print("Sweet! I found a Pouch of gold coins...")
        elif treasure == 10:
            print("Cool! I found some Golden Jewlery...")
        elif treasure == 6:
            print("Nice! I found a rare Gem")
        elif treasure == 6:
            print("WOW! I found a Treasure!")
        else:
            print("...Nothing in here...")

    def set_position(self, position):
        self.current_position = position
