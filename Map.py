from Room import Room

## There probably is a better way but, I create a map template with "X"s and then replace all the "X"s with room objects
## and give them the correct room_index
class Map:
    def __init__(self, size=4, player_position=(0, 0)):
        self.map = [["X"] * size for i in range(size)]
        for row in range(size):
            for room in range(size):
                self.map[row][room] = Room((row, room))

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

    def print_map(self):
        for row in self.map:
            print(row)
        print("-------------------")

    def move_player(self, position):
        x, y = position
