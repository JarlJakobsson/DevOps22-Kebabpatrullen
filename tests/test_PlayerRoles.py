from PlayerRoles import Knight, Thief, Wizard


def test_knight():
    knight = Knight()
    assert knight.initiative == 5
    assert knight.health == 9
    assert knight.attack == 6
    assert knight.agility == 4
    assert knight.max_health == 9
    assert knight.role == "Knight"
    assert knight.block is True


def test_thief():
    thief = Thief()
    assert thief.initiative == 7
    assert thief.health == 5
    assert thief.attack == 5
    assert thief.agility == 7
    assert thief.max_health == 5
    assert thief.role == "Thief"


def test_wizard():
    wizard = Wizard()
    assert wizard.initiative == 6
    assert wizard.health == 5
    assert wizard.attack == 9
    assert wizard.agility == 5
    assert wizard.max_health == 5
    assert wizard.role == "Wizard"
