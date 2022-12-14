from Room import Room


def test_set_visited():
    room = Room()
    room.set_visited()
    assert room.visited is True


def test_remove_monster():
    room = Room()
    room.remove_monster()
    assert room.monster == 0


def test_remove_treasure():
    room = Room()
    room.remove_treasure()
    assert room.treasure == 0
