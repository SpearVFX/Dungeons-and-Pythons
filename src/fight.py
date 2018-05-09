from src.hero import Hero
from src.enemy import Enemy
from src.fight_status_bar import FightStatusBar

import pdb

class Fight:
    def __init__(self,*, hero, enemy,dungeon):
        self.hero = hero
        self.enemy = enemy
        self.dungeon = dungeon
        self.winner = None
        
        self.range_ = self.calculate_range(hero.get_coords(),
                                           enemy.get_coords())
        self.battle_log = ''  # needed when displaying info
        self.status_bar = FightStatusBar(self.hero, self.enemy,self.dungeon)
        

    def calculate_range(self, heroCoords, enemyCoords):
        if heroCoords[0] == enemyCoords[0]:
            return abs(heroCoords[1] - enemyCoords[1])
        elif heroCoords[1] == enemyCoords[1]:
            return abs(heroCoords[0] - enemyCoords[0])
        else:
            return -1
    
    """
        Sets the winner attribute, depending on who's still alive. 
    """

    def __set_winner(self):
        self.winner = self.hero if self.hero_won_the_fight() else self.enemy

    """
        Returns true if the hero is alive.
    """

    def hero_won_the_fight(self):
        return self.hero.is_alive()

    def initialize_fight(self):
        if self.range_ == -1:
            print("Invalid fight")
        self.status_bar.header_string_with_clear_terminal()
        fight_turn = True
        """
        Since it's a turn based fight the bool will represent the turn:
        if fight_turn is True the Hero attacks
        if fight_turn is False the Enemy attacks
        """
    
        while(self.both_alive()):
            if fight_turn:
                print("Your turn: ")
                self.hero_attack()

            else:
                self.enemy_attack()

            self.battle_log += (f'Current range is: {self.range_} \n')
            self.status_bar.header_string_with_clear_terminal()
            print(self.battle_log)
            if not fight_turn:
                self.battle_log = ''
            fight_turn = not fight_turn  # switch turns
        

        #pdb.set_trace()
        self.__set_winner()
        return True
        

    def both_alive(self):
        if not self.hero.is_alive():
            print(f'{self.hero.known_as()} is dead. Game over.')
            return False
        elif not self.enemy.is_alive():
            print(f'Enemy is dead.')
            return False
        else:
            return True

    def spell_is_in_range(self, e):
        if e.get_spell().get_castRange() >= self.range_:
            return True
        else:
            return False

    def damage_report(self, attacker, damage, sw, victim):
        a = attacker
        d = damage
        s = sw
        v = victim
        return(f'{a} dealt {d} with {s} to {v} \n')

    def hero_attack(self):
        spell_ = self.hero.get_spell()
        weapon_ = self.hero.get_weapon()
        print("Spell or Weapon?   -   Enter s or w \n")
        command = input()
        if command == "s":
            if self.hero.can_cast() and self.spell_is_in_range(self.hero):
                self.enemy.take_damage(self.hero.attack(by="spell"))
                self.battle_log += (self.damage_report(
                                    self.hero.get_name(),
                                    spell_.get_damage(),
                                    str(spell_),
                                    self.enemy.get_name()))
            else:
                self.battle_log += f'Cannot cast spell. \n'
                if self.range_ != 0:
                    self.battle_log += ("Moving forward 1 Unit. \n")
                    self.dungeon.chase(chaser=self.hero, chased=self.enemy)
                    self.range_ -= 1
        
        elif command == 'w':
            if self.range_ != 0:
                self.battle_log += ("Cannot attack with weapon. \
                Moving forward 1 unit. \n")
                self.dungeon.chase(chaser=self.hero, chased=self.enemy)

            else:
                self.enemy.take_damage(self.hero.attack(by="weapon"))
                self.battle_log += (self.damage_report(
                                    self.hero.get_name(),
                                    weapon_.get_damage(),
                                    str(weapon_),
                                    self.enemy.get_name()))


    def enemy_attack(self):
        spell_ = self.enemy.get_spell()
        weapon_ = self.enemy.get_weapon()

        if self.enemy.can_cast() and self.spell_is_in_range(self.enemy):
            self.hero.take_damage(self.enemy.attack(by="spell"))
            self.battle_log += (self.damage_report(
                  self.enemy.get_name(),
                  spell_.get_damage(),
                  str(spell_),
                  self.hero.get_name()))
        elif self.range_ == 0:
            self.hero.take_damage(self.enemy.get_base_damage())
            self.battle_log += (self.damage_report(
                  self.enemy.get_name(),
                  self.enemy.get_base_damage(),
                  str(weapon_),
                  self.hero.get_name()))
        elif self.range_ >0:
            self.battle_log += ("Enemy cannot attack. Moving 1 UNIT. \n")
            self.dungeon.chase(chaser=self.enemy, chased=self.hero)
            self.range_ -= 1


    def get_winner(self):
        return self.winner