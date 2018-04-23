class Entity:

    def __init__(self, *, name = None, health = 0, mana = 0):
        self.__name = name
        self.__health = health
        self.__mana = mana

''' Checks if the Entity is alive. '''
    def is_alive(self):
        return True if self.__health else False
''' Checks if the Entity has enough mana to cast. '''
    def can_cast(self):
        return True if self.__mana else False

''' Getter methods '''
    def get_health(self):
        return self.__health
    def get_mana(self):
        return self.__mana
    def get_name(self):
        return self.__name