import pytest

from Map import Map


@pytest.fixture
def map():
    return Map()


def test_init(map):
    assert map.size == 4
    assert map.player_position == (0, 0)
    assert map.map[0][0].__class__.__name__ == "Room"


def test_mark_player_position(map):
    map.mark_player_position((1, 1))
    assert map.map[1][1].name == "P"


def test_mark_visited_room(map):
    map.mark_visited_room((1, 1))
    assert map.map[1][1].name == "0"


def test_mark_player_leave_room(map):
    map.mark_player_position((1, 1))
    map.mark_player_leave_room()
    assert map.map[1][1].name == "0"
