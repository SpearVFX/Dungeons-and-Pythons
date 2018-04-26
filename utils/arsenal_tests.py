import unittest

from arsenal import Arsenal
from weapon import Weapon
from spell import Spell


class ArsenalUnitTests(unittest.TestCase):
    
    def setUp(self):
        self.dummy = Arsenal()
        self.weapon = Weapon(name = "Gorehowl", damage = 20)
        self.spell = Spell(name = "Pyroblast", damage = 40, manaCost= 30, castRange = 1)

    def test_Arsenal_equip_weapon_method(self):
        self.dummy.equip_weapon(weapon=self.weapon)
    
    def test_Arsenal_learn_spell_method(self):
        self.dummy.learn_spell(spell=self.spell)

    def test_Arsenal_getters(self):
        
        self.dummy.equip_weapon(weapon=self.weapon)
        
        with self.subTest("Test Arsenal get weapon method."):
            self.assertEqual(self.dummy.get_weapon(), self.weapon)
        
        self.dummy.learn_spell(spell=self.spell)
        
        with self.subTest("Test Arsenal get spell method."):
            self.assertEqual(self.dummy.get_spell(), self.spell)
        
if __name__ == '__main__':
    unittest.main()
