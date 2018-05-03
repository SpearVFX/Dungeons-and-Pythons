from weapon import Weapon
from spell import Spell
from arsenal import Arsenal


class Entity:
    def __init__(self, *, name=None, health=0, mana=0):
        self.__name = name
        self.coordinates = (0,0)

        self.__maxHealth = health
        self.__maxMana = mana

        self.__currHealth = self.__maxHealth
        self.__currMana = self.__maxMana

        self.__arsenal = Arsenal()

    ''' Sets the current arsenal weapon to the passed in one. '''
    
    def equip(self, weapon):
        self.__arsenal.equip_weapon(weapon=weapon)

    ''' Sets the current arsenal spell to the passed in one. '''

    def learn(self, spell):
        self.__arsenal.learn_spell(spell=spell)

    ''' Returns the damage dealth by the specific source. '''
    def attack(self, *, by=""):
        if by == "weapon":
            return self.__arsenal.get_weapon().get_damage()
        elif by == "spell":
            self.__currMana -= self.__arsenal.get_spell().get_manaCost()
            return self.__arsenal.get_spell().get_damage()
        else:
            raise ValueError(f'Argument- by can only be: weapon, spell.\n')

    '''Returns the amount of health gained after an event has occured.'''

    def __calculate_health_gain(self, health=0):
        if self.__currHealth + health <= self.__maxHealth:
            return health
        else:
            return self.__maxHealth - self.__currHealth

    '''Returns the amount of mana gained after an event has occured.'''

    def __calculate_mana_gain(self, mana=0):

        if self.__currMana + mana <= self.__maxMana:
            return mana
        else:
            return self.__maxMana - self.__currMana

    ''' Current stats modifier methods. '''

    def take_damage(self, damage=0):
        self.__currHealth -= damage


    ''' Sums the healing points returned by the __calculate_health_gain method and the currentHealth. '''

    def take_mana(self, mana=0):
        self.__currMana += self.__calculate_mana_gain(mana)

    ''' Sums the healing points returned by the __calculate_health_gain method and the currentHealth. '''
    
    def take_healing(self, healingPoints=0):
        self.__currHealth += self.__calculate_health_gain(healingPoints)

    ''' Checks if the Entity is alive. '''

    def is_alive(self):
        return self.__currHealth > 0


    ''' Checks if the Entity has enough mana to cast. '''
    
    def can_cast(self):
        return (self.__currMana - self.__arsenal.get_spell().get_manaCost()) >= 0
    
    ''' Sets the entities current coords to x and y. '''
    
    def set_coords(self,*, x, y):
        self.coordinates = (x,y)

    ''' Getter methods '''

    def get_health(self):
        return self.__currHealth

    def get_mana(self):
        return self.__currMana

    def get_max_health(self):
        return self.__maxHealth

    def get_max_mana(self):
        return self.__maxMana

    def get_name(self):
        return self.__name

    def get_weapon(self):
        return self.__arsenal.get_weapon()

    def get_spell(self):
        return self.__arsenal.get_spell()

    def get_coords(self):
        return self.coordinates
