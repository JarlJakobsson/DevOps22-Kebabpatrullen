import random
class Character():
    def __init__(self) -> None:
        current_position = self.current_position
        is_alive = self.is_alive

    def attack_roll(attack_stat):
        attack_value = random.randint(0,6) * attack_stat
        print(f'i try attack ({attack_value} attack roll')
        return attack_value

    def death(self):
        self.is_alive = False
        print('im death gg')

    def dodge_roll(self, dodge_stat):
        dodge_value = random.randint(0,6) * dodge_stat
        print(f'i try dodge ({dodge_value} dodge roll)')
        return dodge_value

    def set_position(self, position):
        self.current_position = position