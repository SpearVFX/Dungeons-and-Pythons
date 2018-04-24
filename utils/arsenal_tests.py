import unittest

from arsenal import Arsenal
from weapon import Weapon
from spell import Spell


class ArsenalUnitTests(unittest.TestCase):
    def test_Arsenal_object_creation(self):
        weapon = Weapon("Gorehowl", 20)
        spell = Spell("Pyroblast", 40, 30, 1)
        dummy = Arsenal(weapon, spell)
        

if __name__ == '__main__':
    unittest.main()
