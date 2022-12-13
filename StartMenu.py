from constants import MAIN_MENU_TEXT, NAME_TEXT, ROLE_TEXT
from utils.visuals import (ascii_02, ascii_knight, ascii_thief, ascii_wizard,
                           clear)

# from SaveLoad import Load


class Start_menu:
    def __init__(self):
        self.name = ""
        self.role = 0

    def wait_for_user(self):
        if self.keep_going:
            input("\nPress Enter to continue...")

    def user_choice(self):
        return input("Enter your choice:")

    def choose_name(self):
        clear()
        print(ascii_02)

        self.name = input(NAME_TEXT)
        while True:
            if self.name == "":
                print("[GAME] Thats not a valid name...")
                self.wait_for_user()
                self.choose_name()
            else:

                break

    def choose_role(self):
        clear()
        print(ascii_02)
        self.choice = input(ROLE_TEXT)
        if self.choice == "1":
            self.role = 1
            clear()
            print(ascii_knight)
        elif self.choice == "2":
            self.role = 2
            clear()
            print(ascii_wizard)
        elif self.choice == "3":
            self.role = 3
            clear()
            print(ascii_thief)
        else:
            self.role = 4
            print("Thats not a valid choice...")
            # self.wait_for_user() # I think it was me who commented this out, but it might be needed for sending the user back to the menu

    def menu_commands(self, choice):
        if choice == "1":
            self.choose_name()
            self.choose_role()
            while True:
                if self.role == 4:
                    self.choose_role()
                else:
                    break
        elif choice == "2":
            print("*** WIP ***")
        elif choice == "3":
            self.keep_going = False

    def run_menu(self):
        self.keep_going = True
        while self.keep_going:  # Not totally sure about this double while loop
            self.input = input(MAIN_MENU_TEXT)  # Probably we should call user_choice() here
            while True:
                if self.input == "":
                    self.input = input(MAIN_MENU_TEXT)
                else:
                    break
            self.menu_commands(self.input)
            print(self.name)
            print(self.role)
            break
