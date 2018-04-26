from entity import Entity

class Hero(Entity):
    def __init__(self, name="", title="", health=100,
                 mana=100, mana_regeneration_rate=2):

        super().__init__(name = name, health = health, mana = mana)
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return f'{super().get_name()} the {self.__title}'
