from random import randint

from Player import Player

player = Player()


def test_get_treasure():
    player.get_treasure(2)
    assert player.treasure_value == 2
    player.get_treasure(6)
    assert player.treasure_value == 8
    player.get_treasure(10)
    assert player.treasure_value == 18


def test_escape_roll():
    escape = randint(1, 100)
    if escape <= 10 * player.agility:
        assert player.escape_roll() is True
    else:
        assert player.escape_roll() is False


def test_set_position():
    player.set_position(5)
    assert player.current_position == 5


def test_move():
    player.move()
