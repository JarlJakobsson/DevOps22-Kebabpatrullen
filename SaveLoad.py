# Use csv to save and load data


class Save:
    def __init__(self, name, character, score):
        self.name = name
        self.character = character
        self.score = score

# Save on a new line in the csv file
    def save_data(self):
        with open("save_data.csv", "a") as f:
            f.write(f"{self.name},{self.character},{self.score}\n")


# Load a name from the csv file if that name exists in the file
class Load:
    def __init__(self, name):
        self.name = name

# Looked in the csv file for the name, if it exists, load the data
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
            except IndexError:
                print("Name not found")
