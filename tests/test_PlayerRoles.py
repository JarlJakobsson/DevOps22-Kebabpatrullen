
# from PlayerRoles import Knight, Thief, Wizard

# # I need a position from class Player, probably not done yet

# def test_Knight_init():
#     knight = Knight()
#     assert knight.initiative == 5
#     assert knight.health == 9
#     assert knight.attack == 6
#     assert knight.agility == 4
#     assert knight.max_health == 9
#     assert knight.is_knight is True
#     assert knight.block_rdy is True


# def test_Knight_set_block():
#     knight = Knight()
#     knight.set_block()
#     assert knight.block_rdy is False


# def test_Wizard_init():
#     wizard = Wizard()
#     assert wizard.initiative == 6
#     assert wizard.health == 5
#     assert wizard.attack == 9
#     assert wizard.agility == 5
#     assert wizard.max_health == 5
#     assert wizard.is_wizard is True


# def test_Wizard_escape_roll():
#     wizard = Wizard()
#     assert wizard.escape_roll() is True or wizard.escape_roll() is False


# def test_Thief_init():
#     thief = Thief()
#     assert thief.initiative == 7
#     assert thief.health == 5
#     assert thief.attack == 5
#     assert thief.agility == 7
#     assert thief.max_health == 5
#     assert thief.is_thief is True


# def test_Thief_attack_roll():
#     thief = Thief()
#     assert thief.attack_roll() is True or thief.attack_roll() is False
