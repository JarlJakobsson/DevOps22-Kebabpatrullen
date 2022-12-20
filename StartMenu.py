import json

from constants import (ASCII_KNIGHT, ASCII_THIEF, ASCII_WIZARD, LOAD_TEXT,
                       MAIN_MENU_TEXT, NAME_TEXT, RAIDERS, ROLE_TEXT,
                       SIZE_TEXT, START_TEXT)
from utils import visuals


class Start_menu:
    """ The start menu for the game. """

    def __init__(self):
        self.name = ""
        self.role = 0
        self.keep_going = True
        self.role = 0
        self.score = 0
        with open("save_data.json", "r") as f:
            self.data = json.loads(f.read())

    def print_saved_characters(self):
        """ Prints all saved characters """
        visuals.clear()
        for key in self.data.keys():
            print(
                f"{key} | {self.data[key]['role']} | {self.data[key]['score']} Kebabs"
            )
            print("-----------------------------")

    def load_data(self, load_name):
        """ Loads data from save_data.json """
        self.load = False
        while True:
            if load_name in self.data.keys():
                self.load = True
                self.name = load_name
                self.role = self.data[load_name]["role"]
                self.score = int(self.data[load_name]["score"])
                break
            elif load_name == "q":
                break
            else:
                visuals.clear()
                print("Name not found.")
                input("Press Enter...")
                self.print_saved_characters()
                load_name = input(LOAD_TEXT)

    def choose_name(self):
        """ Asks for a name and checks if its valid. """
        self.name = input(NAME_TEXT)
        while True:
            if self.name == "":
                print("[GAME] Thats not a valid name...")
                self.choose_name()
            elif self.name in self.data.keys():
                print("Name already taken.")
                self.choose_name()
            else:
                break

    def wait_input(self):
        """ Waits for input. """
        input("Press Enter...")

    def art_and_load(self, art):
        """ Prints ascii art and waits for input."""
        visuals.clear()
        print(art)
        self.wait_input()
        print("")

    def choose_role(self):
        """ Asks for a role and checks if its valid. """
        print(ASCII_KNIGHT)
        self.wait_input()
        print(ASCII_WIZARD)
        self.wait_input()
        print(ASCII_THIEF)
        self.wait_input()
        self.choice = input(ROLE_TEXT)
        if self.choice == "1":
            self.art_and_load(ASCII_KNIGHT)
            self.role = "Knight"
        elif self.choice == "2":
            self.art_and_load(ASCII_WIZARD)
            self.role = "Wizard"
        elif self.choice == "3":
            self.art_and_load(ASCII_THIEF)
            self.role = "Thief"
        else:
            self.role = 0
            print("Thats not a valid choice...")
        while True:
            if not self.role:
                self.choose_role()
            else:
                break

    def choose_size(self):
        """ Asks for a size and checks if its valid. """
        self.choice = input(SIZE_TEXT)
        if self.choice == "1":
            self.size = 4
        elif self.choice == "2":
            self.size = 5
        elif self.choice == "3":
            self.size = 8
        else:
            print("Thats not a valid choice...")
            self.size = 0
        while True:
            if not self.size:
                self.choose_size()
            else:
                break

    def choose_start(self):
        """ Asks for a start position and checks if its valid. """
        self.choice = input(START_TEXT)
        if self.choice == "1":
            self.start = (0, 0)
        elif self.choice == "2":
            self.start = (0, self.size - 1)
        elif self.choice == "3":
            self.start = (self.size - 1, 0)
        elif self.choice == "4":
            self.start = (self.size - 1, self.size - 1)
        else:
            print("Thats not a valid choice...")
            self.start = 0
        while True:
            if not self.start:
                self.choose_start()
            else:
                break

    def add_player(self):
        """ Adds the player to save_data.json """
        self.data[self.name] = {"role": self.role, "score": 0}

    def menu_commands(self):
        """ The main menu. """
        self.load = False
        visuals.clear()
        print(RAIDERS)
        self.choice = input(MAIN_MENU_TEXT)
        if self.choice == "1":
            self.load = True
            self.choose_name()
            self.choose_role()
            self.choose_size()
            self.choose_start()
            self.add_player()
        elif self.choice == "2":
            self.print_saved_characters()
            self.load_data(input(LOAD_TEXT))
            if self.load:
                self.choose_size()
                self.choose_start()
        elif self.choice == "q":
            self.keep_going = False
            return
        else:
            print("Thats not a valid choice...")
            self.choice = 0
        while True:
            if not self.choice or not self.load:
                self.menu_commands()
            else:
                break

    def run_menu(self):
        """ Runs the menu. """
        self.keep_going = True
        while self.keep_going:
            self.menu_commands()
            break
