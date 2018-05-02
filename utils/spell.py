class Spell:
    def __init__(self, *, name="", damage=0, manaCost=0, castRange=0):
        self.__name = name
        self.__damage = damage
        # the spell needs at least that much amount of mana in order to be
        # cast.
        self.__manaCost = manaCost
        # Raise an error if you cannot cast that spell.
        # if cast range is 1 you can attack enemies next you.
        self.__castRange = castRange

    def __str__(self):
        return f'{self.__name}, damage: {self.__damage}, cost: {self.__manaCost}, range: {self.__castRange}.'

    def get_damage(self):
        return self.__damage

    def get_manaCost(self):
        return self.__manaCost

    def get_castRange(self):
        return self.__castRange
