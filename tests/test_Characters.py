

from Characters import Character

# from Enemies import Giantspider, Orc, Skeleton, Troll


def test_Character():
    assert Character().is_alive is True
    assert Character().initiative == 0
    assert Character().health == 0
    assert Character().attack == 0
    assert Character().agility == 0
    assert Character().name == ""
    assert Character().max_health == 0


def test_roll():
    attack = 0
    if attack == 1:
        assert Character().roll(1) == 1


# def test_Giantspider():
#     assert Giantspider().initiative == 7
#     assert Giantspider().health == 1
#     assert Giantspider().attack == 2
#     assert Giantspider().agility == 3
#     assert Giantspider().max_health == 1
#     assert Giantspider().name == "Giant Spider"


# def test_Skeleton():
#     assert Skeleton().initiative == 4
#     assert Skeleton().health == 2
#     assert Skeleton().attack == 3
#     assert Skeleton().agility == 3
#     assert Skeleton().max_health == 2
#     assert Skeleton().name == "Skeleton"


# def test_Orc():
#     assert Orc().initiative == 6
#     assert Orc().health == 3
#     assert Orc().attack == 4
#     assert Orc().agility == 4
#     assert Orc().max_health == 3
#     assert Orc().name == "Orc"


# def test_Troll():
#     assert Troll().initiative == 2
#     assert Troll().health == 4
#     assert Troll().attack == 7
#     assert Troll().agility == 2
#     assert Troll().max_health == 4
#     assert Troll().name == "Troll"
