
"""
In order for our hero to have proper damage,
he must be equiped with either a weapon or a spell.
One hero can carry at max 1 weapon and 1 spell.
"""


class Weapon:
    def __init__(self, *, name="", damage=0)
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name


class Spell:
    def __init__(self, *, name="",damage=0, mana_cost=0, cast_range=0)
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost # the spell needs at least that much amount of mana in order to be cast.
                                   # Raise an error if you cannot cast that spell.
        self.cast_range = cast_range # if cast range is 1 you can attack enemies next you.

    def __str__(self):
        return self.name
