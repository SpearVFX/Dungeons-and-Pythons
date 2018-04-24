from weapon import Weapon
from spell import Spell
from decorators.decorators import accepts

class Arsenal:
    
    @accepts(Weapon, Spell)
    def __init__(self, weapon = None, spell = None):
        self.__weapon = weapon
        self.__spell = spell

    @accepts(Weapon)
    def equip_weapon(self, weapon = None):
        self.__weapon = weapon

    @accepts(Spell)
    def learn_spell(self, spell= None):
        self.__spell = spell