from Characters import Character


class Giantspider(Character):
    def __init__(self):
        super().__init__()
        self.initiative = 7
        self.health = 1
        self.attack = 2
        self.agility = 3
        self.max_health = 1
        self.name = "Giant Spider"


class Skeleton(Character):
    def __init__(self):
        super().__init__()
        self.initiative = 4
        self.health = 2
        self.attack = 3
        self.agility = 3
        self.max_health = 2
        self.name = "Skeleton"


class Orc(Character):
    def __init__(self):
        super().__init__()
        self.initiative = 6
        self.health = 3
        self.attack = 4
        self.agility = 4
        self.max_health = 3
        self.name = "Orc"


class Troll(Character):
    def __init__(self):
        super().__init__()
        self.initiative = 2
        self.health = 4
        self.attack = 7
        self.agility = 2
        self.max_health = 4
        self.name = "Troll"
