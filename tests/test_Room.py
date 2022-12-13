import Room as r


def test_room_init():
    room = r.Room()
    assert room.visited is False
    assert room.monster == 0
    assert room.treasure == 0


def test_set_visited():
    room = r.Room()
    room.set_visited()
    assert room.visited is True


def test_remove_monster():
    room = r.Room()
    room.remove_monster()
    assert room.monster == 0


def test_remove_treasure():
    room = r.Room()
    room.remove_treasure()
    assert room.treasure == 0
