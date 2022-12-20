from constants import RAIDERS, KEBAB, BATTLE_TEXT, ASCII_WALL, EXIT_TEXT
from PlayerRoles import Knight, Thief, Wizard
from BattleMenu import Battle_menu
from StartMenu import Start_menu
from MoveMenu import Move_menu
from threading import Thread
from Monsters import Death
from utils import visuals
from Map import Map
import pygame
import json
import os


class Game:
    def __init__(self):
        self.start_menu = Start_menu()
        self.move_menu = Move_menu()
        self.battle_menu = Battle_menu()
        self.map = 0
        self.player = 0
        self.old_position = (0,)
        self.escaped = False
        self.secret = False
        self.wall_count = 0
        pygame.init()

    def wait_input(self):
        input("\nPress Enter...\n")

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
    def post_combat(self, position):
        if self.player.health:
            self.player.get_treasure(self.map.map[position[0]][position[1]].treasure)
            self.remove_treasure_and_moster(position)
            self.wait_input()

    def remove_treasure_and_moster(self, position):
        self.map.map[position[0]][position[1]].monster = 0
        self.map.map[position[0]][position[1]].treasure = 0

    def check_room(self, position):
        visuals.clear()
        self.map.print_map()
        # Check if self.map.map[x][y].monster is True. If True prints the monster name, activates knight block, starts battle
        # If player escaped calls move back method, else post_combat cleanup
        if self.map.map[position[0]][position[1]].monster:
            print(self.map.map[position[0]][position[1]].monster.ascii)
            self.play_music("battle_music.mp3")
            self.wait_input()
            self.knight_block()
            self.battle_method(self.map.map[position[0]][position[1]].monster)
            self.play_music("music.mp3")
        else:
            print(f"\n{self.player.name}: ...No monsters in here...\n")
        if self.escaped:
            self.move_back()
        else:
            self.post_combat(position)
            if self.map.map[position[0]][position[1]].have_secret:
                print(f"{self.player.name}: This room smell of Kebab... And evil...")
                self.wait_input()

    # Method to move player back to previous room (used after succesful escape)
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

    # Method to check compare initative rolls and decide who starts the battle
    def initiative_method(self, monster):
        if self.player.initative_roll() >= monster.initative_roll():
            self.first = self.player
            self.second = monster
            print(f"\n***  {self.player.name} takes initative! ***")
        else:
            print(f"\n*** {monster.name} takes initatitve! ***")
            self.first = monster
            self.second = self.player

    def battle_art(self, monster):
        self.wait_input()
        visuals.clear()
        print(monster.ascii)
        print(monster.name + " : " + "[]" * monster.health)
        print("")
        print(self.player.name + " : " + "[]" * self.player.health)
        print(BATTLE_TEXT)

    def swap_atk(self):
        # Swaps first and second
        temp = self.second
        self.second = self.first
        self.first = temp

    # Calls initative method to check who starts, if atk_value >= dodge, second takes dmg
    def battle_method(self, monster):
        self.initiative_method(monster)
        while True:
            self.battle_art(monster)
            self.first.attack_roll()
            if self.first.atk_value == 0:
                # Heals monster if player escape
                monster.heal()
                self.escaped = True
                break
            elif self.first.atk_value == 1:
                print(f"{self.second.name} attacks {self.first.name}")
                self.first.take_dmg()
                if not self.first.health:
                    break
            elif self.first.atk_value >= self.second.dodge_roll():
                self.second.take_dmg()
                if not self.second.health:
                    break
            else:
                print(f"\n*** {self.second} dodged the attack! ***")
            self.swap_atk()

    def move_player(self, direction, position):
        # Adds direction to player position and saves old player position (incase of Move back after battle escape)
        x = position[0] + direction[0]
        y = position[1] + direction[1]
        current_room = self.map.map[position[0]][position[1]]
        self.old_position = position

        # Checks if new room exists. Adds a counter for moving into a wall, calls take_dmg if counter reaches 2
        # And checks if players health is not 0
        if x == -1 or x > self.map.size - 1 or y == -1 or y > self.map.size - 1:
            if current_room.have_secret and self.wall_count == 1:
                current_room.have_secret = False
                self.secret = True
                print(f"*** {self.player.name} charges into the wall head first ***")
                self.wait_input()
                return True
            print(ASCII_WALL)
            print(f"{self.player.name}: Ouch... There is a wall there...")
            self.wall_count += 1
            self.wait_input()
            if self.wall_count == 2:
                self.player.take_dmg()
                self.wall_count = 0
                self.wait_input()
                if not self.player.health:
                    print(f"*** {self.player.name} was killed by a wall ***")
                    self.wait_input()
                    print(ASCII_WALL)
                    self.wait_input()
                    return True
            return False
        # If exists, Marks current room as visited, Updates player location, Marks new room as currently in
        else:
            self.map.mark_visited_room(position)
            self.map.player_position = (x, y)
            self.map.mark_player_position(self.map.player_position)
            return True

    def check_exit(self, position):
        if self.map.map[position[0]][position[1]].have_exit:
            self.choice = input(EXIT_TEXT)
            if self.choice == "1":
                return False
            elif self.choice == "2":
                self.play_music("kebab_win.mp3")
                print(
                    f"\n*** YOU ESCAPED WITH TREASURES WORTH {self.player.score} KEBABS ***"
                )
                self.wait_input()
                visuals.clear()
                print(f"Thank you for playing\n{RAIDERS}\n")
                self.wait_input()
                self.save_method()
                self.play_music("music.mp3")
                self.player.exits = True
                return True
            else:
                print("Thats not a choice...")
                self.check_exit(position)
        else:
            return False

    def secret_battle(self):
        self.secret = False
        print("\n*** You found a secret door! ***\n")
        self.wait_input()
        death = Death()
        self.first = self.player
        self.second = death
        print(death.ascii)
        self.play_music("persona_boss.mp3")
        self.wait_input()
        self.battle_method(death)
        if self.player.health and not self.escaped:
            self.play_music("kebab_win.mp3")
            visuals.clear()
            print("*** The smell of Evil is gone, but the smell of Kebab is not... ***")
            self.wait_input()
            print(f"*** {self.player.name} looks around and cannot believe it ***")
            self.wait_input()
            visuals.clear()
            print(KEBAB)
            self.wait_input()

    def save_method(self):
        with open("save_data.json", "w+") as f:
            self.start_menu.data[self.player.name]["score"] = self.player.score
            new_data = json.dumps(self.start_menu.data)
            f.write(new_data)
            print("\n*** Character saved ***")
            self.wait_input()

    def game_over_method(self):
        self.play_music("death_music.mp3")
        visuals.clear()
        self.start_menu.data.pop(self.player.name)
        with open("save_data.json", "w+") as f:
            new_data = json.dumps(self.start_menu.data)
            f.write(new_data)
        print(RAIDERS)
        print(
            "                         *** GAME OVER - YOUR CHARACTER IS NO MORE... ***\n"
        )
        self.wait_input()

    def play_music(self, filename):
        current_dir = os.getcwd()
        file_path = current_dir + filename
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def main(self):
        stop_thread = Thread(target=pygame.mixer.music.stop)
        stop_thread.start()
        while True:
            self.play_music("music.mp3")
            self.music = Thread(target=pygame.mixer.music.play)
            self.start_menu.run_menu()
            if not self.start_menu.keep_going:
                pygame.quit()
                break
            self.create_player(self.start_menu.role)
            self.map = Map(self.start_menu.size, self.start_menu.start)
            self.map.mark_player_position(self.map.player_position)
            self.remove_treasure_and_moster(self.map.player_position)
            while True:
                if not self.player.health:
                    self.game_over_method()
                    break
                if self.move_menu.quit == True:
                    self.move_menu.quit = False
                    print("\nReturning to Start menu...")
                    self.wait_input()
                    break
                self.check_room(self.map.player_position)
                if not self.player.health:
                    self.game_over_method()
                    break
                self.check_exit(self.map.player_position)
                if self.player.exits:
                    break
                while True:
                    self.map.print_map()
                    self.move_menu.run_menu()
                    if self.move_menu.quit == True:
                        break
                    if self.move_player(
                        self.move_menu.direction, self.map.player_position
                    ):
                        if self.secret == True:
                            self.secret_battle()
                            self.play_music("music.mp3")
                        break


if __name__ == "__main__":
    game = Game()
    game.main()
