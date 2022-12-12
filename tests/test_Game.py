from Game import Game
from MoveMenu import Move_menu
from PlayerRoles import Knight, Thief, Wizard
from StartMenu import Start_menu

game = Game()


def test_game_init():
    assert game.map == 0
    assert game.player == 0
    assert isinstance(game.start_menu, Start_menu)
    assert isinstance(game.move_menu, Move_menu)
    assert game.initiatior == 0


def test_create_player():
    game.create_player(1)
    assert isinstance(game.player, Knight)
    game.create_player(2)
    assert isinstance(game.player, Wizard)
    game.create_player(3)
    assert isinstance(game.player, Thief)
