from Room import Room


def test_summon_monster():
    room = Room()
    assert room.monster is not None


def test_create_treasure():
    room = Room()
    assert room.treasure is not None


def test_repr():
    room = Room()
    assert room.__repr__() == "X"
