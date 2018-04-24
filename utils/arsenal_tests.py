import unittest

from arsenal import Arsenal
from weapon import Weapon
from spell import Spell


class ArsenalUnitTests(unittest.TestCase):
    
    def test_Arsenal_object_creation(self):
        
        weapon = Weapon(name = "Gorehowl", damage = 20)
        spell = Spell(name = "Pyroblast", damage = 40, manaCost= 30, castRange = 1)
        dummy = Arsenal(weapon, spell)


if __name__ == '__main__':
    unittest.main()
