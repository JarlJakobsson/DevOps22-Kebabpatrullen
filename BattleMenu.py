

class Battle_menu:
    """ This class is used to create a menu for the battle system. """

    def __init__(self):
        pass

    def run_menu(self):
        """ This method is used to run the menu. """
        self.choice = input("What will you do?\n")
        if self.choice == "1":
            self.choice = 1
        elif self.choice == "2":
            self.choice = 0
        else:
            print("Thats not a choice...\n")
            self.choice = 2
        while True:
            if self.choice == 2:
                self.run_menu()
            else:
                break
