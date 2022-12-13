import unittest

from Room import Room


class TestRoom(unittest.TestCase):
    def test_room_init(self):
        room = Room()
        self.assertEqual(room.visited, False)
        self.assertEqual(room.monster, 0)
        self.assertEqual(room.treasure, 0)

    def test_set_visited(self):
        room = Room()
        room.set_visited()
        self.assertEqual(room.visited, True)

    def test_remove_monster(self):
        room = Room()
        room.remove_monster()
        self.assertEqual(room.monster, 0)

    def test_remove_treasure(self):
        room = Room()
        room.remove_treasure()
        self.assertEqual(room.treasure, 0)


if __name__ == "__main__":
    unittest.main()
