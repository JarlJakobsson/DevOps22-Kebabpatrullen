import Map as m


def test_create_map():
    map = m.Map()
    map.create_map(4)
    assert map.map == [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]


def test_mark_player_position():
    map = m.Map()
    map.create_map(4)
    map.mark_player_position(1, 1)
    assert map.map == [['X', 'X', 'X', 'X'], ['X', 'P', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]


def test_mark_visited_room():
    map = m.Map()
    map.create_map(4)
    map.mark_player_position(1, 1)
    map.mark_visited_room(1, 1)
    assert map.map == [['X', 'X', 'X', 'X'], ['X', '0', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]


def test_give_player_position():
    pass
