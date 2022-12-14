from Characters import Character


def test_init():
    character = Character()
    assert character.is_alive is True
    assert character.initiative == 0
    assert character.health == 0
    assert character.attack == 0
    assert character.agility == 0
    assert character.name == ""
    assert character.max_health == 0
    assert character.role == ""


def test_roll_dice():
    character = Character()
    assert 1 <= character.roll_dice() <= 6


def test_attack_roll():
    character = Character()
    assert 0 <= character.attack_roll() <= 6


def test_initative_roll():
    character = Character()
    assert 0 <= character.initative_roll() <= 6


def test_dodge_roll():
    character = Character()
    assert 0 <= character.dodge_roll() <= 6


def test_death():
    character = Character()
    character.death()
    assert character.is_alive is False


def test_take_dmg():
    character = Character()
    character.take_dmg()
    assert character.health == -1


def test_roll():
    character = Character()
    assert 0 <= character.roll(1) <= 6


def test_heal():
    character = Character()
    character.heal()
    assert character.health == 0
