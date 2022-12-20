
from Game import Game
from PlayerRoles import Knight, Thief, Wizard


def test_Game_init():
    game = Game()
    assert game.player is not None


def test_create_player():
    game = Game()
    game.create_player("Knight")
    assert isinstance(game.player, Knight)
    game.create_player("Thief")
    assert isinstance(game.player, Thief)
    game.create_player("Wizard")
    assert isinstance(game.player, Wizard)
