from constants import (
    MAIN_MENU_TEXT,
    NAME_TEXT,
    ROLE_TEXT,
    SIZE_TEXT,
    START_TEXT,
    LOAD_TEXT,
    ASCII_WIZARD,
    ASCII_KNIGHT,
    ASCII_THIEF
)
from utils import visuals
import json
import textwrap
import shutil

class Start_menu:
    def __init__(self):
        self.name = ""
        self.role = 0
        self.keep_going = True
        self.role = 0
        self.score = 0
        with open("save_data.json", "r") as f:
            self.data = json.loads(f.read())


    def print_saved_characters(self):
        visuals.clear()
        for key in self.data.keys():
            print(
                f"{key} | {self.data[key]['role']} | {self.data[key]['score']} Kebabs"
            )
            print("-----------------------------")

    def load_data(self, load_name):
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
        input("Press Enter...")

    def art_and_load(self, art):
        visuals.clear()
        print(art)
        visuals.loading_bar()
        print("")
        visuals.clear()

    def choose_role(self):
        print(ASCII_KNIGHT)
        self.wait_input()
        print(ASCII_WIZARD)
        self.wait_input()
        print(ASCII_THIEF)
        self.wait_input()
        self.choice = input(ROLE_TEXT)
        if self.choice == "1":
            # self.art_and_load(visuals.ascii_knight)
            self.role = "Knight"
        elif self.choice == "2":
            # self.art_and_load(visuals.ascii_wizard)
            self.role = "Wizard"
        elif self.choice == "3":
            # self.art_and_load(visuals.ascii_thief)
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
        self.data[self.name] = {"role": self.role, "score": 0}

    def menu_commands(self):
        self.choice = input(MAIN_MENU_TEXT)
        if self.choice == "1":
            self.choose_name()
            self.choose_role()
            self.choose_size()
            self.choose_start()
            self.add_player()
        elif self.choice == "2":
            self.print_saved_characters()
            self.load_data(input(LOAD_TEXT))
            self.choose_size()
            self.choose_start()
        elif self.choice == "3":
            self.keep_going = False
        else:
            print("Thats not a valid choice...")
            self.choice = 0
        while True:
            if not self.choice:
                self.menu_commands()
            else:
                break

    def run_menu(self):
        self.keep_going = True
        while self.keep_going:
            self.menu_commands()
            break