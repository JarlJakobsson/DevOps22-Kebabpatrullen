import unittest

from Characters import Character


class TestCharacter:
    def test_init(self):
        character = Character()
        assert character.is_alive is True
        assert character.initiative == 0
        assert character.health == 0
        assert character.attack == 0
        assert character.agility == 0
        assert character.name == ""
        assert character.max_health == 0
        assert character.role == ""

    def test_roll_dice(self):
        character = Character()
        assert 1 <= character.roll_dice() <= 6

    def test_attack_roll(self):
        character = Character()
        assert 0 <= character.attack_roll() <= 6

    def test_initative_roll(self):
        character = Character()
        assert 0 <= character.initative_roll() <= 6

    def test_dodge_roll(self):
        character = Character()
        assert 0 <= character.dodge_roll() <= 6

    def test_death(self):
        character = Character()
        character.death()
        assert character.is_alive is False

    def test_take_dmg(self):
        character = Character()
        character.take_dmg()
        assert character.health == -1


if __name__ == "__main__":
    unittest.main()
