class Map:
    def __init__(self):
        self.map = [[]]
        self.is_start = True

    def create_map(self, size):
        self.map = [["X"] * size for i in range(size)]

    def mark_player_position(self, pos1, pos2):
        self.map[pos1][pos2] = "P"

    def mark_visited_room(self, pos1, pos2):
        self.map[pos1][pos2] = "0"

    def give_player_position(self, current):
        pass
