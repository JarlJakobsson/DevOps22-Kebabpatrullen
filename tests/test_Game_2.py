import pytest

from Game import Game
from PlayerRoles import Knight, Thief, Wizard


@pytest.fixture
def game():
    return Game()


def test_create_player(game):
    game.create_player("Knight")
    assert isinstance(game.player, Knight)
    assert game.player.name == game.start_menu.name
    assert game.player.score == game.start_menu.score

    game.create_player("Wizard")
    assert isinstance(game.player, Wizard)
    assert game.player.name == game.start_menu.name
    assert game.player.score == game.start_menu.score

    game.create_player("Thief")
    assert isinstance(game.player, Thief)
    assert game.player.name == game.start_menu.name
    assert game.player.score == game.start_menu.score


def test_knight_block(game):
    game.create_player("Knight")
    game.knight_block()
    assert game.player.block
