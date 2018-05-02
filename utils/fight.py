from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.range = self.calculate_range(hero.get_coords(), enemy.get_coords())

    def calculate_range(self, heroCoords, enemyCoords):
        if heroCoords[0] == enemyCoords[0]:
            return abs(heroCoords[1] - enemyCoords[1])
        elif heroCoords[1] == enemyCoords[1]:
            return abs(heroCoords[0] - enemyCoords[0])
        else:
            return -1

    def initialize_fight(self):
        if self.range == -1:
            print("Invalid fight!!!")
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
            if self.hero.can_cast() and spell_is_in_range(self.hero):
                self.enemy.take_damage(spell_.get_damage())
                self.hero.take_mana(spell_.get_manaCost())
                print(f'{self.hero.get_name()} dealt {spell_.get_damage()} to {self.enemy.get_name()}')
            else:
                print("Cannot cast spell. Moving forward 1 UNIT.")
                self.range -= 1
        elif command == 'w':
            if range != 1:
                print("Cannot attack with weapon. Moving forward 1 UNIT.")
            else:
                self.enemy.take_damage(weapon_.get_damage())
                print(f'{self.hero.get_name()} dealt {weapon_.get_damage()} with {weapon_.get_name()} to {self.enemy.get_name()}')
    def enemy_attack(self):
        pass
    @staticmethod
    def spell_is_in_range(entity):
        if entity.get_spell().get_castRange() >= range:
            return True
        else:
            return False



    def enemy_attack(self):
        pass
