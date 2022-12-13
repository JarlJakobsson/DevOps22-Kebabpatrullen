import os
import sys
import time

ascii_01 = """
██████  ██    ██ ███    ██  ██████  ███████  ██████  ███    ██     ██████  ██    ██ ███    ██ 
██   ██ ██    ██ ████   ██ ██       ██      ██    ██ ████   ██     ██   ██ ██    ██ ████   ██ 
██   ██ ██    ██ ██ ██  ██ ██   ███ █████   ██    ██ ██ ██  ██     ██████  ██    ██ ██ ██  ██ 
██   ██ ██    ██ ██  ██ ██ ██    ██ ██      ██    ██ ██  ██ ██     ██   ██ ██    ██ ██  ██ ██ 
██████   ██████  ██   ████  ██████  ███████  ██████  ██   ████     ██   ██  ██████  ██   ████ 
                                                                                              
                                                                                              """

ascii_02 = """
██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗    ██████╗ ██╗   ██╗███╗   ██╗
██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║    ██╔══██╗██║   ██║████╗  ██║
██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║    ██████╔╝██║   ██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║    ██╔══██╗██║   ██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║    ██║  ██║╚██████╔╝██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

ascii_03 = """
▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █     ██▀███   █    ██  ███▄    █
▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █    ▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █
░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒   ▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒
░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒   ▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒
░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░   ░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒
 ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░     ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░
 ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░      ░░   ░  ░░░ ░ ░    ░   ░ ░
   ░       ░              ░       ░    ░  ░    ░ ░           ░       ░        ░              ░
 ░
 """

ascii_04 = """
██   ██ ███████ ██████   █████  ██████  ██████   █████  ████████ ██████  ██    ██ ██      ██      ███████ ███    ██ 
██  ██  ██      ██   ██ ██   ██ ██   ██ ██   ██ ██   ██    ██    ██   ██ ██    ██ ██      ██      ██      ████   ██ 
█████   █████   ██████  ███████ ██████  ██████  ███████    ██    ██████  ██    ██ ██      ██      █████   ██ ██  ██ 
██  ██  ██      ██   ██ ██   ██ ██   ██ ██      ██   ██    ██    ██   ██ ██    ██ ██      ██      ██      ██  ██ ██ 
██   ██ ███████ ██████  ██   ██ ██████  ██      ██   ██    ██    ██   ██  ██████  ███████ ███████ ███████ ██   ████ 
                                                                                                                    
"""


ascii_knight = """
██   ██ ███    ██ ██  ██████  ██   ██ ████████ 
██  ██  ████   ██ ██ ██       ██   ██    ██    
█████   ██ ██  ██ ██ ██   ███ ███████    ██
██  ██  ██  ██ ██ ██ ██    ██ ██   ██    ██
██   ██ ██   ████ ██  ██████  ██   ██    ██
                                            
"""

ascii_thief = """
████████ ██   ██ ██ ███████ ███████ 
   ██    ██   ██ ██ ██      ██      
   ██    ███████ ██ █████   █████
   ██    ██   ██ ██ ██      ██    
   ██    ██   ██ ██ ███████ ██
                               
"""

ascii_wizard = """
██     ██ ██ ███████  █████  ██████  ██████
██     ██ ██    ███  ██   ██ ██   ██ ██   ██ 
██  █  ██ ██   ███   ███████ ██████  ██   ██ 
██ ███ ██ ██  ███    ██   ██ ██   ██ ██   ██ 
 ███ ███  ██ ███████ ██   ██ ██   ██ ██████  
                                            
"""

ascii_battle = """
██████   █████  ████████ ████████ ██      ███████ 
██   ██ ██   ██    ██       ██    ██      ██      
██████  ███████    ██       ██    ██      █████
██   ██ ██   ██    ██       ██    ██      ██    
██████  ██   ██    ██       ██    ███████ ███████ 
                                                  
"""

ascii_won = """
██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██ 
   ██     ██████   ██████       ███ ███   ██████  ██   ████ 
                                                            
"""

ascii_lost = """
██    ██  ██████  ██    ██     ██       ██████  ███████ ████████ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██    
  ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██
   ██    ██    ██ ██    ██     ██      ██    ██      ██    ██
   ██     ██████   ██████      ███████  ██████  ███████    ██
                                                              
"""


USER_MOVE_VARIANT = "\n\tUp(W)\n Left(A)\tRight(D) \n\tDown(S)\n\r> "


def clear():
    """Clears the screen in terminal, works on all OS"""
    os.system('cls' if os.name == 'nt' else 'clear')


def loading_bar():  # Pragma: no cover
    """Prints a loading bar, just to fake a loading time"""
    print("\nLoading...")
    for i in range(0, 105, 5):
        time.sleep(0.1)
        sys.stdout.write("\r" + str(i+1) + "%")
        sys.stdout.flush()


def intro_screen():  # Pragma: no cover
    """Prints the intro screen, one of the ascii art above"""
    clear()
    print(ascii_03)
    print("Welcome to Dungeon Run!")


def sleep(x):  # Pragma: no cover
    """Sleeps for x seconds, just to give the player time to read the text"""
    time.sleep(x)


def instruction_short():  # Pragma: no cover
    instructions = """

This is a text-based adventure game. You will be presented with a series of choices.
You will be able to choose between 1-4 options. You will be able to type the number
of the option you want to choose. For example, if you want to choose option 2, you
will type 2 and press enter.

Good luck!


If you need help, you can ask the game developers for help
They are nice people. You find them by this name:
"""
    print(instructions)
    sleep(3)
    print(ascii_04)
    input("Press enter to continue...")
    clear()


def outro_screen():  # Pragma: no cover
    """Prints the outro screen, at the end of the game"""
    clear()
    print("Thank you for playing ")
    print(ascii_02)
    exit()


def knight_art():   # Pragma: no cover
    """Prints the knight ascii art"""
    clear()
    print(ascii_knight)
    sleep(1)


def thief_art():   # Pragma: no cover
    """Prints the thief ascii art"""
    clear()
    print(ascii_thief)
    sleep(1)


def wizard_art():  # Pragma: no cover
    """Prints the wizard ascii art"""
    clear()
    print(ascii_wizard)
    sleep(1)
