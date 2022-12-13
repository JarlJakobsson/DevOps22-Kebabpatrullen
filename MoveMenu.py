from constants import MOVE_MENU_TEXT


class Move_menu:
    def __init__(self):
        pass

    def run_menu(self):
        self.choosing = True
        self.direction = (0,)
        self.choice = input(MOVE_MENU_TEXT)

        if self.choice == "w":
            self.direction = (-1, 0)

        elif self.choice == "s":
            self.direction = (1, 0)

        elif self.choice == "a":
            self.direction = (0, -1)

        elif self.choice == "d":
            self.direction = (0, 1)
        else:
            print("Thats not a direction...\n")
            input("Press any key")
            self.direction = 0

        while True:
            if not self.direction:
                self.run_menu()
            else:
                break
