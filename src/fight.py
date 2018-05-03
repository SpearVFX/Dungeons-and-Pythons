from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.range_ = self.calculate_range(hero.get_coords(), enemy.get_coords())

    def calculate_range(self, heroCoords, enemyCoords):
        if heroCoords[0] == enemyCoords[0]:
            return abs(heroCoords[1] - enemyCoords[1])
        elif heroCoords[1] == enemyCoords[1]:
            return abs(heroCoords[0] - enemyCoords[0])
        else:
            return -1

    def initialize_fight(self):
        if self.range_ == -1:
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

            print("Hero has ", self.hero.get_health())
            print("Enemy has ", self.enemy.get_health())
            if not self.hero.is_alive():
                print(f'{self.hero.known_as()} is dead. Game over.')
                both_alive = False
            elif not self.enemy.is_alive():
                print(f'Enemy is dead.')
                both_alive = False
            fight_turn = not fight_turn #  switch turns
        return

    def spell_is_in_range(self, e):
        if e.get_spell().get_castRange() >= self.range_:
            return True
        else:
            return False


    def hero_attack(self):
        spell_ = self.hero.get_spell()
        weapon_ = self.hero.get_weapon()
        print("Spell or Weapon?   -   Enter s or w")
        command = input()
        if command == "s":
            if self.hero.can_cast() and self.spell_is_in_range(self.hero):
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print(f'{self.hero.get_name()} dealt {spell_.get_damage()} with with {str(spell_)} to {self.enemy.get_name()}')
            else:
                print("Cannot cast spell. Moving forward 1 UNIT.")
                self.range_ -= 1
        elif command == 'w':
            if self.range_ != 0:
                print("Cannot attack with weapon. Moving forward 1 UNIT.")
            else:
                self.enemy.take_damage(self.hero.attack(by="weapon"))
                print(f'{self.hero.get_name()} dealt {weapon_.get_damage()} with {str(weapon_)} to {self.enemy.get_name()}')

    def enemy_attack(self):
        spell_ = self.enemy.get_spell()
        weapon_ = self.enemy.get_weapon()

        if self.enemy.can_cast() and self.spell_is_in_range(self.enemy):
            self.hero.take_damage(self.enemy.attack(by="spell"))
            print(f'{self.enemy.get_name()} dealt {spell_.get_damage()} with with {str(spell_)} to {self.hero.get_name()}')
        elif self.range_ == 0:
            self.hero.take_damage(self.enemy.attack(by="weapon"))
            print(f'{self.enemy.get_name()} dealt {weapon_.get_damage()} with with {str(weapon_)} to {self.hero.get_name()}')
        else:
            print("Enemy cannot attack. Moving 1 UNIT.")
            self.range_ -= 1
