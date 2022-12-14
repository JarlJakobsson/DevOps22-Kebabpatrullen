from constants import BATTLE_TEXT
from utils import visuals

class Battle_menu:
    def __init__(self):
        pass

    def run_menu(self):
        self.choice = input(BATTLE_TEXT)
        if self.choice == "1":
            return 1
        elif self.choice == "2":
            return 0
        else:
            print("Thats not a choice...\n")
            input("Press any key")
            self.choice = 2
        while True:
            if self.choice is 2:
                self.run_menu()
            else:
                break
