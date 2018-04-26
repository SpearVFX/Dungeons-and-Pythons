from entity import Entity
from weapon import Weapon
from spell import Spell


class Hero(Entity):
    def __init__(self, name="", title="", health=100,
                 mana=100, mana_regeneration_rate=2):

        self.super().__init__(name = name, health = health, mana = mana)
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate
