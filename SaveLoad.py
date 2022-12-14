
class Save:
    """Save data to a csv file. For keep it simple, i'm using a csv file instead of a database."""
    def __init__(self, name, character, score):
        self.name = name
        self.character = character
        self.score = score

    def save_data(self):
        with open("save_data.csv", "a") as f:
            f.write(f"{self.name},{self.character},{self.score}\n")


class Load:
    def __init__(self, name):
        self.name = name

    def load_data(self):
        with open("save_data.csv", "r") as f:
            try:
                f.readline()
                for line in f.readlines():
                    data = line.split(",")
                    if data[0] == self.name:
                        self.name = data[0]
                        self.character = data[1]
                        self.score = data[2]
                        break
            except AttributeError:
                print("Name not found")
