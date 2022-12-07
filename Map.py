class Map:
    def __init__(self, size = 4):
        self.map = [["X"] * size for i in range(size)]
        self.is_start = True

    # def create_map(self, size=4):
    #     self.map = [["X"] * size for i in range(size)]

    def mark_player_position(self, pos1, pos2):
        self.map[pos1][pos2] = "P"

    def mark_visited_room(self, pos1, pos2):
        self.map[pos1][pos2] = "0"

    def give_player_position(self, current):
        pass
