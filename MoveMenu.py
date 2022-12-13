from constants import MOVE_MENU_TEXT

# from utils.visuals import USER_MOVE_VARIANT_3


class Move_menu:
    def __init__(self):
        pass

    def run_menu(self):
        self.choosing = True
        self.direction = (0,)
        self.choice = input(MOVE_MENU_TEXT)  # Jarl version
        # self.choice = input(USER_MOVE_VARIANT_3) # Alex version

        if self.choice == "1" or self.choice == "w":
            self.direction = (-1, 0)

        elif self.choice == "2" or self.choice == "s":
            self.direction = (1, 0)

        elif self.choice == "3" or self.choice == "a":
            self.direction = (0, -1)

        elif self.choice == "4" or self.choice == "d":
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
