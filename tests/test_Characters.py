
from Characters import Character


def test_init():
    character = Character()
    assert character.is_alive is True
    assert character.initiative == 0
    assert character.health == 0
    assert character.attack == 0
    assert character.agility == 0
    assert character.max_health == 0
    assert character.name == ""
    assert character.role == ""
    assert character.ascii == ""


def test_roll_dice():
    character = Character()
    assert character.roll_dice() in range(1, 7)


def test_heal():
    character = Character()
    character.health = 5
    character.max_health = 10
    character.heal()
    assert character.health == 10


def test_repr():
    character = Character()
    character.name = "Test"
    assert character.__repr__() == "Test"
