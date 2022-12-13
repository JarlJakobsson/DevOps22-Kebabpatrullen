import unittest
from unittest.mock import patch

from StartMenu import Start_menu


class TestStartMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Start_menu()

    def test_choose_name(self):
        with patch('builtins.input', return_value='Test'):
            self.menu.choose_name()
            self.assertEqual(self.menu.name, 'Test')

    def test_choose_role(self):
        with patch('builtins.input', return_value='1'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 1)
        with patch('builtins.input', return_value='2'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 2)
        with patch('builtins.input', return_value='3'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 3)
        with patch('builtins.input', return_value='4'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 4)

    def test_menu_commands(self):
        with patch('builtins.input', return_value='1'):
            self.menu.menu_commands('1')
            self.assertEqual(self.menu.role, 1)
        with patch('builtins.input', return_value='2'):
            self.assertEqual(self.menu.menu_commands('2'), None)
        with patch('builtins.input', return_value='3'):
            self.menu.menu_commands('3')
            self.assertEqual(self.menu.keep_going, False)

    def test_run_menu(self):
        with patch('builtins.input', return_value='1'):
            self.menu.run_menu()
            self.assertEqual(self.menu.role, 1)


if __name__ == '__main__':
    unittest.main()
