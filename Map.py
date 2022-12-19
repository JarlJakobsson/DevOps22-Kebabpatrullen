from Room import Room
from random import randint, choice
from utils import visuals

## There probably is a better way but, I create a map template with "X"s and then replace all the "X"s with room objects
## and give them the correct room_index
class Map:
    def __init__(self, size=4, player_position=(0, 0)):
        self.map = [["X"] * size for i in range(size)]
        for row in range(size):
            for col in range(size):
                self.map[row][col] = Room()

        rand_row = randint(0, size - 1)
        rand_col = randint(0, size - 1)
        self.map[rand_row][rand_col].monster = 0
        self.map[rand_row][rand_col].treasure = 0
        self.map[rand_row][rand_col].have_exit = True
        # self.map[rand_row][rand_col].name = "E"  # REMOVE LATER
        secret_row = [0, size - 1]
        secret_col = [0, size - 1]
        secret_rand_row = choice(secret_row)
        secret_rand_col = choice(secret_col)
        self.map[secret_rand_row][secret_rand_col].have_secret = True
        self.is_start = True
        self.size = size
        self.player_position = player_position

    def mark_player_position(self, position):
        x, y = position
        self.map[x][y].name = "P"

    def mark_visited_room(self, position):
        x, y = position
        self.map[x][y].name = "0"

    def mark_player_leave_room(self):
        for row in range(self.size):
            for room in range(self.size):
                if self.map[row][room].name == "P":
                    self.map[row][room].name = "0"

    # Method to print the map. And some bad math to try and get "Map" centered and boarder scaling with size
    def print_map(self):
        visuals.clear()
        print(" " * (self.size + 1) + "MAP")
        print("#" * (self.size * 3))
        for row in self.map:
            print(row)
        print("#" * (self.size * 3))
