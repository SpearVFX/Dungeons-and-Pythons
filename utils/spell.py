class Spell:
    def __init__(self, *, name="",damage=0, manaCost=0, castRange=0):
        self.__name = name
        self.__damage = damage
        self.__manaCost = manaCost # the spell needs at least that much amount of mana in order to be cast.
                                   # Raise an error if you cannot cast that spell.
        self.__castRange = castRange # if cast range is 1 you can attack enemies next you.

    def __str__(self):
        return f'{self.__name}, damage: {self.__damage}, cost: {self.__manaCost}, range: {self.__castRange}.'

    def get_damage(self):
        return self.__damage
    
    def get_manaCost(self):
        return self.__manaCost
    
    def get_castRange(self):
        return self.__castRange