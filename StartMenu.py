from constants import MAIN_MENU_TEXT, NAME_TEXT, ROLE_TEXT
import constants
from time import sleep
from utils import visuals


class Start_menu:
    def __init__(self):
        self.name = ""
        self.role = 0
        self.keep_going = True

    def choose_name(self):
        self.name = input(NAME_TEXT)
        while True:
            if self.name == "":
                print("[GAME] Thats not a valid name...")
                self.choose_name()
            else:
                break

    def art_and_load(self, art):
        visuals.clear()
        print(art)
        visuals.loading_bar()
        print("")
        visuals.clear()

    def choose_role(self):
        self.choice = input(ROLE_TEXT)
        if self.choice == "1":
            self.art_and_load(visuals.ascii_knight)
            self.role = 1
        elif self.choice == "2":
            self.art_and_load(visuals.ascii_wizard)
            self.role = 2
        elif self.choice == "3":
            self.art_and_load(visuals.ascii_thief)
            self.role = 3
        else:
            self.role = 0
            print("Thats not a valid choice...")
        while True:
            if not self.role:
                self.choose_role()
            else:
                break

    def menu_commands(self):
        self.choice = input(MAIN_MENU_TEXT)
        if self.choice == "1":
            self.choose_name()
            self.choose_role()
        elif self.choice == "2":
            print("*** WIP ***")
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
