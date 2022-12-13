from constants import BATTLE_TEXT


class Battle_menu:
    def __init__(self):
        pass

    def run_menu(self):
        self.choice = input(BATTLE_TEXT)
        if self.choice == "1":
            return 1
        elif self.choice == "2":
            2
        else:
            print("Thats not a choice...\n")
            input("Press any key")
            self.choice = 0
        while True:
            if not self.choice:
                self.run_menu()
            else:
                break
