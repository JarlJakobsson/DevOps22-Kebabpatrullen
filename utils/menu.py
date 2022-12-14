from utils.visuals import (clear, instruction_short, intro_screen, knight_art,
                           loading_bar, outro_screen, sleep, thief_art,
                           wizard_art)

player_name = ""
player_character = ""
board_style = "ascii"
board_size = 4


class Menu:

    def __init__(self, title, options, actions, exit=False, back=False):
        self.title = title
        self.options = options
        self.actions = actions
        self.exit = exit
        self.back = back

    def display(self):
        """Display the menu"""
        clear()
        print(self.title)
        print("=" * len(self.title))
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")
        print()
        if self.back:
            print(f"{len(self.options) + 1}. Back")
        if self.exit:
            print(f"{len(self.options) + 1}. Exit")
        print()
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice >= 1 and choice <= len(self.options) + 1:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid choice. Try again.")

    def handle_choice(self, choice):
        """Handle the choice"""
        if choice == len(self.options) + 1 and self.back:
            return "back"
        elif choice == len(self.options) + 1 and self.exit:
            return "exit"
        else:
            return self.actions[choice - 1]


main_menu = Menu(
    "Dungeon Run",
    ["Play", "Highscore", "Help", "Settings"],
    ["play", "highscore", "help", "settings"],
    True,
)

play_menu = Menu(
    "Play",
    ["New player", "Load player"],
    ["new_player", "load_player"],
    False,
    True,
)

highscore_menu = Menu(
    "Highscore",
    ["View highscore", "Reset highscore"],
    ["view_highscore", "reset_highscore"],
    False,
    True,
)

help_menu = Menu(
    "Help",
    ["View instructions"],
    ["view_instructions"],
    False,
    True,
)

settings_menu = Menu(
    "Settings",
    ["Change board style"],
    ["change_board_style"],
    False,
    True,
)

character_menu = Menu(
    "Choose Character",
    ["Knight", "Wizard", "Thief"],
    ["knight", "wizard", "thief"],
    False,
    True,
)

change_map_size_menu = Menu(
    "Choose map size",
    ["Small", "Medium", "Big"],
    ["small_map", "medium_map", "big_map"],
    False,
    True,
)

change_board_style_menu = Menu(
    "Change board style",
    ["Ascii", "Emoji", "GUI"],
    ["ascii_map", "emoji_map", "gui_map"],
    False,
    True,
)


load_name_menu = Menu(
    "Load name",
    ["Alex", "Frida", "Jarl", "Mandana", "Raffi"],
    ["load_name_1", "load_name_2", "load_name_3", "load_name_4", "load_name_5"],
    False,
    True,
)


def show_menu(menu):
    """Show the menu and handle the choice"""
    choice = menu.display()
    return menu.handle_choice(choice)


def play():
    """Show the play menu"""
    while True:
        choice = show_menu(play_menu)
        if choice == "new_player":
            new_player()
        elif choice == "load_player":
            load_player()
        elif choice == "back":
            break


def new_player():
    """Create a new player"""
    global player_name
    clear()
    player_name = input("Enter your name: ")
    print(f"Welcome {player_name}!")
    sleep(1)
    load_character()


def load_player():
    """Load a player"""
    while True:
        choice = show_menu(load_name_menu)
        if choice == "load_name_1":
            load_name_1()
        elif choice == "load_name_2":
            load_name_2()
        elif choice == "load_name_3":
            load_name_3()
        elif choice == "load_name_4":
            load_name_4()
        elif choice == "load_name_5":
            load_name_5()
        elif choice == "back":
            break


def load_character():
    """ Load the character """
    while True:
        choice = show_menu(character_menu)
        if choice == "knight":
            knight()
        elif choice == "wizard":
            wizard()
        elif choice == "thief":
            thief()
        elif choice == "back":
            break


def settings():
    """Show the settings menu"""
    while True:
        choice = show_menu(settings_menu)
        if choice == "change_board_style":
            change_board_style()
        elif choice == "back":
            break


def change_map_size():
    """Change the map size"""
    while True:
        choice = show_menu(change_map_size_menu)
        if choice == "small_map":
            small_map()
        elif choice == "medium_map":
            medium_map()
        elif choice == "big_map":
            big_map()
        elif choice == "back":
            break


def small_map():
    """Set the map size to small"""
    global board_size
    board_size = 4
    print("Map size changed to small!")
    sleep(1)
    clear()
    load_game()


def medium_map():
    """Set the map size to medium"""
    global board_size
    board_size = 5
    print("Map size changed to medium!")
    sleep(1)
    clear()
    load_game()


def big_map():
    """Set the map size to big"""
    global board_size
    board_size = 8
    print("Map size changed to big!")
    sleep(1)
    clear()
    load_game()


def change_board_style():
    """Change the board style"""
    while True:
        choice = show_menu(change_board_style_menu)
        if choice == "ascii_map":
            ascii_map()
        elif choice == "emoji_map":
            emoji_map()
        elif choice == "gui_map":
            gui_map()
        elif choice == "back":
            break


def load_name():
    """Load the name"""
    while True:
        choice = show_menu(load_name_menu)
        if choice == "load_name_1":
            load_name_1()
        elif choice == "load_name_2":
            load_name_2()
        elif choice == "load_name_3":
            load_name_3()
        elif choice == "load_name_4":
            load_name_4()
        elif choice == "load_name_5":
            load_name_5()
        elif choice == "back":
            break


def highscore():
    """Show the highscore menu"""
    while True:
        choice = show_menu(highscore_menu)
        if choice == "view_highscore":
            view_highscore()
        elif choice == "reset_highscore":
            reset_highscore()
        elif choice == "back":
            break


def view_highscore():
    """View the highscore"""
    print("Viewing highscore...")
    sleep(1)
    clear()
    print("Highscore viewed!")
    sleep(1)
    clear()
    starting_menu()


def reset_highscore():
    """Reset the highscore"""
    print("Resetting highscore...")
    sleep(1)
    clear()
    print("Highscore reset!")
    sleep(1)
    clear()
    starting_menu()


def help():
    """Show the help menu"""
    while True:
        choice = show_menu(help_menu)
        if choice == "view_instructions":
            view_instructions()
        elif choice == "back":
            break


def view_instructions():
    """View the instructions"""
    print("Loading instructions...")
    sleep(1)
    instruction_short()
    starting_menu()


def load_name_1():
    """Load name 1"""
    global player_name
    player_name = "Alex"
    print(f"Welcome {player_name}!")
    sleep(1)
    clear()
    load_character()


def load_name_2():
    """Load name 2"""
    global player_name
    player_name = "Frida"
    print(f"Welcome {player_name}!")
    sleep(1)
    clear()
    load_character()


def load_name_3():
    """Load name 3"""
    global player_name
    player_name = "Jarl"
    print(f"Welcome {player_name}!")
    sleep(1)
    clear()
    load_character()


def load_name_4():
    """Load name 4"""
    global player_name
    player_name = "Mandana"
    print(f"Welcome {player_name}!")
    sleep(1)
    clear()
    load_character()


def load_name_5():
    """Load name 5"""
    global player_name
    player_name = "Raffi"
    print(f"Welcome {player_name}!")
    sleep(1)
    clear()
    load_character()


def ascii_map():
    """Set the board style to ascii"""
    global board_style
    board_style = "ascii"
    print("Board style changed to ascii!")
    sleep(1)
    clear()
    starting_menu()


def emoji_map():
    """Set the board style to emoji"""
    global board_style
    board_style = "emoji"
    print("Board style changed to emoji!")
    sleep(1)
    clear()
    starting_menu()


def gui_map():
    """Set the board style to gui"""
    global board_style
    board_style = "gui"
    print("Board style changed to gui!")
    sleep(1)
    clear()
    starting_menu()


def knight():
    """Set the character to knight"""
    global player_character
    player_character = "knight"
    knight_art()
    change_map_size()


def wizard():
    """Set the character to wizard"""
    global player_character
    player_character = "wizard"
    wizard_art()
    change_map_size()


def thief():
    """Set the character to thief"""
    global player_character
    player_character = "thief"
    thief_art()
    change_map_size()


def load_game():
    global player_name
    global player_character
    global board_size
    global board_style
    loading_bar()
    clear()
    print("Some test print to check the variables")
    print(f"The player is named {player_name.capitalize()}")
    print(f"The player is a {player_character.upper()}")
    print(f"The map size is {board_size} by {board_size}")
    print(f"The board style (for some extra feature) is {board_style.upper()}")
    input("Press enter to close the game...")
    clear()
    outro_screen()


def starting_menu():
    """ Show the menu """
    while True:
        choice = show_menu(main_menu)
        if choice == "play":
            play()
        elif choice == "highscore":
            highscore()
        elif choice == "help":
            help()
        elif choice == "settings":
            settings()
        elif choice == "exit":
            break


def main():
    intro_screen()
    loading_bar()
    starting_menu()
    outro_screen()


if __name__ == "__main__":
    main()
