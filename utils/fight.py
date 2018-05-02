from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.range = self.calculate_range(hero.get_coords(), enemy.get_coords())

    def calculate_range(self, heroCoords, enemyCoords):
        if heroCoords[0] != enemyCoords[0]:
            return abs(heroCoords[0] - enemyCoords[0])
        else:
            return abs(heroCoords[1] - enemyCoords[1])

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
                self.hero_attack()
            else:
                self.enemy_attack()

            if not self.hero.is_alive():
                print f'{self.hero.known_as()} is dead. Game over.'
                both_alive = False
            elif not self.enemy.is_alive():
                print f'Enemy is dead.'
                both_alive = False
            fight_turn = not fight_turn #  switch turns
        return

    def hero_attack(self):
        spell_ = self.hero.get_spell()
        weapon_ = self.hero.get_weapon()
        print("Spell or Weapon?   -   Enter s or w")
        command = input()
        if command == "s":
            if self.hero.can_cast():
                self.enemy.take_damage(spell_.get_damage())
                self.hero.take_mana(spell_.get_manaCost())
                print(f'{self.hero.get_name()} dealt {spell_.get_damage()} to {self.enemy.get_name()}')
            else:
                print("Cannot cast spell.")



    def enemy_attack(self):
        pass
