from weapon import Weapon
from spell import Spell

class Arsenal:

    def __init__(self, weapon = None, spell = None):
        self.__weapon = weapon
        self.__spell = spell

    def equip_weapon(self, weapon = None):
        self.__weapon = weapon
    
    def learn_spell(self, spell= None):
        self.__spell = spell

