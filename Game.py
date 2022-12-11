from Map import Map
from PlayerRoles import Knight, Thief, Wizard

from MoveMenu import Move_menu
from StartMenu import Start_menu



class Game:
    def __init__(self):
        self.map = 0
        self.player = 0
        self.start_menu = Start_menu()
        self.move_menu = Move_menu()
        self.initiatior = 0

    def wait_input(self):
        input("\nPress any key...\n")

    def create_map(self):
        self.map = Map(int(input("Enter size: ")))

    def create_player(self, role):
        if role == 1:
            self.player = Knight()
        elif role == 2:
            self.player = Wizard()
        elif role == 3:
            self.player = Thief()

    def check_room(self, position):
        # Splits position into x and y
        x, y = position

        # Check if self.map.map[x][y].monster is True. If True prints the monster name and battle menu
        if self.map.map[x][y].monster:
            print(f"{self.player.name}: There is a {self.map.map[x][y].monster.name}")
            self.battle(position)
        else:
            print(f"\n{self.player.name}: ...No monsters in here...\n")

        # After battle, Player loots treasure, monster get removed from room, treasure get removed from room
        self.player.get_treasure(self.map.map[x][y].treasure)
        self.map.map[x][y].monster = 0
        self.map.map[x][y].treasure = 0
        self.wait_input()

    def battle(self, position):
        # Compares player initiative roll against monster initiative roll and sets the winner as initiator
        if (
            self.player.initative_roll()
            >= self.map.map[position[0]][position[1]].monster.initative_roll()
        ):
            self.initiatior = 1
            print("[GAME] Player takes initative")
        else:
            print("[GAME] Monster initatitve")
        self.wait_input()

    def move_player(self, direction):
        # Splits direction and player positon
        x, y = direction
        a, b = self.map.player_position
        a += x
        b += y
        
        # Checks if new room exists
        if a == -1 or a > self.map.size - 1 or b == -1 or b > self.map.size - 1:
            print(f"{self.player.name}: Ouch... There is a wall there...")
            self.wait_input()
            return False
        # If exists, Marks current room as visited, Updates player location, Marks new room as currently in
        else:
            self.map.mark_visited_room(self.map.player_position)
            print(f"*** {a,b} ***")
            self.map.player_position = (a, b)
            self.map.mark_player_position((a, b))
            return True

    def main(self):
        self.start_menu.run_menu()
        print(self.start_menu.role)
        self.create_player(self.start_menu.role)
        self.player.name = self.start_menu.name
        self.map = Map()
        self.map.mark_player_position(self.map.player_position)
        while True:
            self.move_player(self.map.player_position)
            while True:
                self.map.print_map()
                self.move_menu.run_menu()
                if self.move_player(self.move_menu.direction):
                    break


game = Game()
game.main()
