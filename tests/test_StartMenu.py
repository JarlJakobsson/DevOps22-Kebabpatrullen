import unittest
from unittest.mock import patch

from StartMenu import Start_menu


class TestStart_menu(unittest.TestCase):
    def setUp(self):
        self.menu = Start_menu()

    def test_choose_name(self):
        with patch('builtins.input', return_value='Test'):
            self.menu.choose_name()
            self.assertEqual(self.menu.name, 'Test')

    def test_choose_role(self):
        with patch('builtins.input', return_value='1'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 'Knight')

        with patch('builtins.input', return_value='2'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 'Wizard')

        with patch('builtins.input', return_value='3'):
            self.menu.choose_role()
            self.assertEqual(self.menu.role, 'Thief')


if __name__ == '__main__':
    unittest.main()
