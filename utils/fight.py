from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, heroCoords, enemy, enemyCoords):
        self.hero = hero
        self.enemy = enemy
        self.range = calculate_range(heroCoords, enemyCoords)

    def calculate_range(self, heroCoords, enemyCoords):
        return abs(heroCoords - enemyCoords)  # needs to be redone

    def initialize_fight(self):
        fight_turn = True
        """
        Since it's a turn based fight the bool will represent the turn:
        if fight_turn is True the Hero attacks
        if fight_turn is False the Enemy attacks
        """
        both_alive = True  # self explainatory

        while(both_alive):
            if fight_turn:
                initiate_attack(self.hero, self.enemy)
            else:
                initiate_attack(self.enemy, self.hero)
            if not self.hero.is_alive():
                print f'{self.hero.known_as()} is dead.'
                both_alive = False
            elif not self.enemy.is_alive():
                print f'Enemy is dead.'
                both_alive = False
            fight_turn = not fight_turn #  switch turns
        return

    @staticmethod
    def attack(fighter1, fighter2):
        pass
