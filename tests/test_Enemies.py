import unittest

from Enemies import Giantspider, Orc, Skeleton, Troll


class TestEnemies(unittest.TestCase):
    def test_Giantspider(self):
        self.assertEqual(Giantspider().initiative, 7)
        self.assertEqual(Giantspider().health, 1)
        self.assertEqual(Giantspider().attack, 2)
        self.assertEqual(Giantspider().agility, 3)
        self.assertEqual(Giantspider().max_health, 1)
        self.assertEqual(Giantspider().name, "Giant Spider")

    def test_Skeleton(self):
        self.assertEqual(Skeleton().initiative, 4)
        self.assertEqual(Skeleton().health, 2)
        self.assertEqual(Skeleton().attack, 3)
        self.assertEqual(Skeleton().agility, 3)
        self.assertEqual(Skeleton().max_health, 2)
        self.assertEqual(Skeleton().name, "Skeleton")

    def test_Orc(self):
        self.assertEqual(Orc().initiative, 6)
        self.assertEqual(Orc().health, 3)
        self.assertEqual(Orc().attack, 4)
        self.assertEqual(Orc().agility, 4)
        self.assertEqual(Orc().max_health, 3)
        self.assertEqual(Orc().name, "Orc")

    def test_Troll(self):
        self.assertEqual(Troll().initiative, 2)
        self.assertEqual(Troll().health, 4)
        self.assertEqual(Troll().attack, 7)
        self.assertEqual(Troll().agility, 2)
        self.assertEqual(Troll().max_health, 4)
        self.assertEqual(Troll().name, "Troll")


if __name__ == '__main__':
    unittest.main()
