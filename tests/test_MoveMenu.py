from unittest import mock

from MoveMenu import Move_menu


@mock.patch("MoveMenu.input", side_effect=["w", "s", "a", "d", "q"])
def test_run_menu(mock_input):
    move_menu = Move_menu()
    move_menu.run_menu()
    assert move_menu.direction == (-1, 0)

    move_menu.run_menu()
    assert move_menu.direction == (1, 0)

    move_menu.run_menu()
    assert move_menu.direction == (0, -1)

    move_menu.run_menu()
    assert move_menu.direction == (0, 1)

    move_menu.run_menu()
    assert move_menu.quit is True
