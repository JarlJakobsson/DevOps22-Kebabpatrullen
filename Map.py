from random import choice, randint

from Room import Room
from utils import visuals


class Map:
    """ Map class to create a map of rooms and keep track of the player's position on the map."""

    def __init__(self, size=4, player_position=(0, 0)):
        self.size = size
        self.map = [["X"] * size for i in range(size)]
        for row in range(size):
            for col in range(size):
                self.map[row][col] = Room()
        exit_row = randint(0, size - 1)
        exit_col = randint(0, size - 1)
        self.map[exit_row][exit_col].monster = 0
        self.map[exit_row][exit_col].treasure = 0
        self.map[exit_row][exit_col].have_exit = True
        self.outer_rooms = []
        self.find_outer_rooms()
        secret_room_index = choice(self.outer_rooms)
        self.map[secret_room_index[0]][secret_room_index[1]].have_secret = True
        self.map[secret_room_index[0]][secret_room_index[1]].name = "S"
        self.is_start = True
        self.player_position = player_position

    def find_outer_rooms(self):
        """ Method to find the outer rooms of the map. """
        for row in range(self.size):
            for col in range(self.size):
                if row in [0, self.size - 1] or col in [0, self.size - 1]:
                    self.outer_rooms.append((row, col))

    def mark_player_position(self, position):
        """ Method to mark the player's position on the map."""
        x, y = position
        self.map[x][y].name = "P"

    def mark_visited_room(self, position):
        """ Method to mark a room as visited."""
        x, y = position
        self.map[x][y].name = "0"

    def mark_player_leave_room(self):
        """ Method to mark the player's previous position on the map."""
        for row in range(self.size):
            for room in range(self.size):
                if self.map[row][room].name == "P":
                    self.map[row][room].name = "0"

    def print_map(self):
        """ Method to print the map."""
        visuals.clear()
        print(" " * (self.size + 1) + "MAP")
        print("#" * (self.size * 3))
        for row in self.map:
            print(row)
        print("#" * (self.size * 3))
