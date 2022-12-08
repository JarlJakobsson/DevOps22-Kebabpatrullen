from constants import MOVE_MENU_TEXT


class Move_menu:
    def __init__(self):
        pass

    def run_menu(self):
        self.choosing = True
        self.direction = (0,)
        self.choice = input(MOVE_MENU_TEXT)

        if self.choice == "1":
            self.direction = (-1, 0)

        elif self.choice == "2":
            self.direction = (1, 0)

        elif self.choice == "3":
            self.direction = (0, -1)

        elif self.choice == "4":
            self.direction = (0, 1)
        else:
            print("Thats not a direction...\n")
            input("Press any key")
            self.direction = 0

        while True:
            if not self.direction:
                self.direction = self.move_menu()
            else:
                break


direction = 0, 1
print(direction)
