
from Room import Room


def test_create_treasure():
    room = Room((0, 0))
    assert room.treasure in [0, 2, 6, 10, 14, 20]


def test_set_visited():
    room = Room((0, 0))
    room.set_visited()
    assert room.visited is True


def test_remove_monster():
    room = Room((0, 0))
    room.remove_monster()
    assert room.monster == 0


def test_remove_treasure():
    room = Room((0, 0))
    room.remove_treasure()
    assert room.treasure == 0


def test_repr():
    room = Room((0, 0))
    assert room.__repr__() == "X"
