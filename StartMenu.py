from constants import MAIN_MENU_TEXT, NAME_TEXT, ROLE_TEXT

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
        self.name = input(NAME_TEXT)
        while True:
            if self.name == "":
                print("[GAME] Thats not a valid name...")
                self.wait_for_user()
                self.choose_name()
            else:

                break

    def choose_role(self):
        self.choice = input(ROLE_TEXT)
        if self.choice == "1":
            self.role = 1
        elif self.choice == "2":
            self.role = 2
        elif self.choice == "3":
            self.role = 3
        else:
            self.role = 4
            print("Thats not a valid choice...")
            # self.wait_for_user()

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
        while self.keep_going:
            self.input = input(MAIN_MENU_TEXT)
            while True:
                if self.input == "":
                    self.input = input(MAIN_MENU_TEXT)
                else:
                    break
            self.menu_commands(self.input)
            print(self.name)
            print(self.role)
            break
