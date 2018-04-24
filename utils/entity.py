class Entity:
    
    def __init__(self, *, name = None, maxHealth = 0, maxMana = 0):
        self.__name = name
        self.__maxHealth = maxHealth
        self.__maxMana = maxMana
        self.__currHealth = self.__maxHealth
        self.__currMana = self.__currMana

'''Current stats changing methods'''
    def take_damage(self, damage = 0):
        self.__currHealth -= damage
    def take_mana(self, mana = 0):
        self.__currMana +=mana
    def take_healing(self, healingPoints = 0):
        self.__currHealth += healingPoints

''' Checks if the Entity is alive. '''
    def is_alive(self):
        return True if self.__currHealth else False
''' Checks if the Entity has enough mana to cast. '''
    def can_cast(self):
        return True if self.__mana else False

''' Getter methods '''
    def get_health(self):
        return self.__currHealth
    def get_mana(self):
        return self.__currMana
    def get_name(self):
        return self.__name