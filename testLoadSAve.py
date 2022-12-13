
import random

from SaveLoad import Load, Save
from utils.visuals import clear, sleep


def make_list():
    for i in range(5):
        name = ["Alex", "Frida", "Jarl", "Mandana", "Raffi"]
        character = random.choice(["Knight", "Wizard", "Thief"])
        score = random.randint(0, 100)
        save = Save(name[i], character, score)
        save.save_data()


def load_name(name):
    load = Load(name)
    load.load_data()
    clear()
    print(f"Name: {load.name}")
    print(f"Character: {load.character}")
    print(f"Score: {load.score}")


def main():
    # make_list() # Uncomment this line to create a new save_data.csv file
    clear()
    print("The players in the game are: Alex, Frida, Jarl, Mandana, Raffi")
    player_name = input("Enter the name of the player you want to load: ")
    try:
        load_name(player_name)
    except AttributeError:
        print("Name not found")
        sleep(2)
        main()


if __name__ == "__main__":
    main()
