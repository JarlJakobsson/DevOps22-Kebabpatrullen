from Game import Game


def test_Game_init():
    game = Game()
    assert game.map == 0
    assert game.player == 0


def test_create_map():
    game = Game()
    game.create_map()
    assert game.map != 0
