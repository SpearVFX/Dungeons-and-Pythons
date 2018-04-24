class Spell:
    def __init__(self, *, name="",damage=0, manaCost=0, castRange=0):
        self.name = name
        self.damage = damage
        self.manaCost = manaCost # the spell needs at least that much amount of mana in order to be cast.
                                   # Raise an error if you cannot cast that spell.
        self.castRange = castRange # if cast range is 1 you can attack enemies next you.

    def __str__(self):
        return self.name