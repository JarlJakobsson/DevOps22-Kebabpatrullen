
from unittest import TestCase
from unittest.mock import patch

from Game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_init(self):
        self.assertEqual(self.game.map, 0)
        self.assertEqual(self.game.player, 0)
        self.assertEqual(self.game.initiatior, 0)

    def test_wait_input(self):
        with patch('builtins.input', return_value='1'):
            self.game.wait_input()
            self.assertEqual(self.game.player, 0)
