from Map import Map
from PlayerRoles import Knight, Thief, Wizard
from MoveMenu import Move_menu
from StartMenu import Start_menu
from constants import EXIT_TEXT
from BattleMenu import Battle_menu
import json
from utils import visuals


class Game:
    def __init__(self):
        self.start_menu = Start_menu()
        self.move_menu = Move_menu()
        self.battle_menu = Battle_menu()
        self.map = 0
        self.player = 0
        self.initiatior = 0
        self.old_position = (0,)
        self.escaped = False

    def wait_input(self):
        input("\nPress any key...\n")

    def create_map(self):
        self.map = Map(int(input("Enter size: ")))

    def create_player(self, role):
        if role == "Knight":
            self.player = Knight()
        elif role == "Wizard":
            self.player = Wizard()
        elif role == "Thief":
            self.player = Thief()
        self.player.name = self.start_menu.name
        self.player.score = self.start_menu.score

    # After battle, Player loots treasure, monster get removed from room, treasure get removed from room
    def post_combat(self, x, y):
        if self.player.health:
            self.player.get_treasure(self.map.map[x][y].treasure)
            self.remove_treasure_and_moster((x, y))
            self.wait_input()

    def remove_treasure_and_moster(self, position):
        self.map.map[position[0]][position[1]].monster = 0
        self.map.map[position[0]][position[1]].treasure = 0

    def check_room(self, position):
        # Splits position into x and y
        x, y = position
        visuals.clear()
        self.map.print_map()
        # Check if self.map.map[x][y].monster is True. If True prints the monster name and battle menu
        if self.map.map[x][y].monster:
            print(
                f"\n{self.player.name}: There is a {self.map.map[x][y].monster.name} in here ...\n"
            )
            self.knight_block()
            self.battle_method(position)
        else:
            print(f"\n{self.player.name}: ...No monsters in here...\n")
        if self.escaped:
            self.move_back()
        else:
            self.post_combat(x, y)

    def move_back(self):
        self.map.mark_visited_room(self.map.player_position)
        self.map.player_position = self.old_position
        self.map.mark_player_position(self.old_position)
        print(f"\n*** {self.player.name} managed to escape to the previous room! ***\n")
        self.wait_input()
        self.escaped = False

    def knight_block(self):
        if self.player.role == "Knight":
            self.player.block = True

    def initiative_method(self, position):
        if (
            self.player.initative_roll()
            >= self.map.map[position[0]][position[1]].monster.initative_roll()
        ):
            self.initiatior = 1
            print(f"\n***  {self.player.name} takes initative! ***")
        else:
            print(
                f"\n*** {self.map.map[position[0]][position[1]].monster.name} takes initatitve! ***"
            )
            self.initiatior = 0

        if self.initiatior:
            self.first = self.player
            self.second = self.map.map[position[0]][position[1]].monster
        else:
            self.first = self.map.map[position[0]][position[1]].monster
            self.second = self.player
        self.wait_input()

    def battle_method(self, position):
        self.initiative_method(position)
        while True:
            visuals.clear()
            if self.first.attack_roll():
                if self.first.atk_value >= self.second.dodge_roll():
                    self.second.take_dmg()
                    if not self.second.health:
                        break
                else:
                    print(f"\n*** {self.second} dodged the attack! ***")
                    self.wait_input()
                if self.second.attack_roll():
                    if self.second.atk_value >= self.first.dodge_roll():
                        self.first.take_dmg()
                        if not self.first.health:
                            break
                    else:
                        print(f"\n*** {self.first} dodged the attack! ***")
                        self.wait_input()
                else:
                    self.map.map[position[0]][position[1]].monster.heal()
                    self.escaped = True
                    break
            else:
                self.map.map[position[0]][position[1]].monster.heal()
                self.escaped = True
                break

    def move_player(self, direction):
        # Splits direction and player positon
        x, y = direction
        a, b = self.map.player_position
        self.old_position = self.map.player_position
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
            self.map.player_position = (a, b)
            self.map.mark_player_position((a, b))
            return True

    def check_exit(self, position):
        if self.map.map[position[0]][position[1]].have_exit:
            self.choice = input(EXIT_TEXT)
            if self.choice == "1":
                return False
            elif self.choice == "2":
                print(
                    f"\n*** YOU ESCAPED WITH TREASURES WORTH {self.player.score} KEBABS ***"
                )
                self.wait_input()
                visuals.clear()
                print(f"Thank you for playing\n{visuals.ascii_02}\n")
                self.wait_input()
                self.save_method()
                self.player.exits = True
                return True
            else:
                print("Thats not a choice...")
                self.check_exit(position)
        else:
            return False

    def save_method(self):
        with open("save_data.json", "w+") as f:
            self.start_menu.data[self.player.name]["score"] = self.player.score
            new_data = json.dumps(self.start_menu.data)
            f.write(new_data)
            print("\n*** Character saved ***")
            self.wait_input()

    def main(self):
        while True:
            visuals.clear()
            self.start_menu.run_menu()
            if not self.start_menu.keep_going:
                break
            self.create_player(self.start_menu.role)
            self.map = Map(self.start_menu.size, self.start_menu.start)
            self.map.mark_player_position(self.map.player_position)
            self.remove_treasure_and_moster(self.map.player_position)
            while True:
                self.check_room(self.map.player_position)
                if not self.player.health:
                    visuals.clear()
                    self.start_menu.data.pop(self.player.name)
                    print("\n*** GAME OVER - YOUR CHARACTER IS NO MORE ***\n")
                    with open("save_data.json", "w+") as f:
                        new_data = json.dumps(self.start_menu.data)
                        f.write(new_data)
                    print(visuals.ascii_02)
                    self.wait_input()
                    break
                self.check_exit(self.map.player_position)
                if self.player.exits:
                    break
                while True:
                    self.map.print_map()
                    self.move_menu.run_menu()
                    if self.move_player(self.move_menu.direction):
                        break


if __name__ == "__main__":
    game = Game()
    game.main()
