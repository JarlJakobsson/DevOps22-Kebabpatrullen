
from unittest import mock

from BattleMenu import Battle_menu


@mock.patch("BattleMenu.input", side_effect=["1", "2"])
def test_run_menu(mock_input):
    battle_menu = Battle_menu()
    battle_menu.run_menu()
    assert battle_menu.choice == 1

    battle_menu.run_menu()
    assert battle_menu.choice == 0
