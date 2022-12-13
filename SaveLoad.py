# When the game finish, the game will save the game data to the file
# The game data is the player's name, player's character and the score(amount of money)

import json


class Save:

    def __init__(self):
        self.save_data = None
        self.save_file = 'save_data.json'

    def save_game(self, player):
        self.save_data = {
            'name': player.name,
            'character': player.character,
            'score': player.score
        }
        with open(self.save_file, 'w') as file:
            json.dump(self.save_data, file)

    def load_game(self):
        with open(self.save_file, 'r') as file:
            self.save_data = json.load(file)
        return self.save_data


class Load:

    def __init__(self):
        self.load_data = None
        self.load_file = 'save_data.json'

    def load_game(self):
        with open(self.load_file, 'r') as file:
            self.load_data = json.load(file)
        return self.load_data
