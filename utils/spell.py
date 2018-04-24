class Spell:
    def __init__(self, *, name="",damage=0, mana_cost=0, cast_range=0)
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost # the spell needs at least that much amount of mana in order to be cast.
                                   # Raise an error if you cannot cast that spell.
        self.cast_range = cast_range # if cast range is 1 you can attack enemies next you.

    def __str__(self):
        return self.name
