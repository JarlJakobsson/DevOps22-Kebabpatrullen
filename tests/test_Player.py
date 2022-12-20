
from Player import Player

player = Player()


def test_get_treasure():
    player.get_treasure(2)
    assert player.score == 2
    player.get_treasure(6)
    assert player.score == 8
    player.get_treasure(10)
    assert player.score == 18
    player.get_treasure(14)
    assert player.score == 32
    player.get_treasure(20)
    assert player.score == 52


def test_escape_roll():
    assert player.escape_roll() in [True, False]
