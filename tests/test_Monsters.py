from Monsters import Giantspider, Orc, Skeleton, Troll


def test_Giantspider():
    monster = Giantspider()
    assert monster.initiative == 7
    assert monster.health == 1
    assert monster.attack == 2
    assert monster.agility == 3
    assert monster.max_health == 1
    assert monster.name == "Giant Spider"


def test_Skeleton():
    monster = Skeleton()
    assert monster.initiative == 4
    assert monster.health == 2
    assert monster.attack == 3
    assert monster.agility == 3
    assert monster.max_health == 2
    assert monster.name == "Skeleton"


def test_Orc():
    monster = Orc()
    assert monster.initiative == 6
    assert monster.health == 3
    assert monster.attack == 4
    assert monster.agility == 4
    assert monster.max_health == 3
    assert monster.name == "Orc"


def test_Troll():
    monster = Troll()
    assert monster.initiative == 2
    assert monster.health == 4
    assert monster.attack == 7
    assert monster.agility == 2
    assert monster.max_health == 4
    assert monster.name == "Troll"
