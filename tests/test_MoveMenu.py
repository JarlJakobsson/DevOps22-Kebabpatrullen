import unittest
from unittest import TestCase
from unittest.mock import patch

from MoveMenu import Move_menu


class TestMoveMenu(TestCase):
    def setUp(self):
        self.menu = Move_menu()

    def test_run_menu(self):
        with patch('builtins.input', return_value='1'):
            self.menu.run_menu()
            self.assertEqual(self.menu.direction, (-1, 0))
        with patch('builtins.input', return_value='2'):
            self.menu.run_menu()
            self.assertEqual(self.menu.direction, (1, 0))
        with patch('builtins.input', return_value='3'):
            self.menu.run_menu()
            self.assertEqual(self.menu.direction, (0, -1))
        with patch('builtins.input', return_value='4'):
            self.menu.run_menu()
            self.assertEqual(self.menu.direction, (0, 1))


if __name__ == '__main__':
    unittest.main()
