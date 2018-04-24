import unittest
from Entity import Entity


class EntityUnitTest(unittest.TestCase):
    def setUp(self):
        self.dummy = Entity(name="Test", health=150, mana=70)

    def test_if_getters_work_correctly(self):
        
        with self.subTest("Test get_name method."):
            self.assertEqual(self.dummy.get_name(), "Test")
        
        with self.subTest("Test get_health method."):
            self.assertEqual(self.dummy.get_health(), 150)
        
        with self.subTest("Test get_mana method."):
            self.assertEqual(self.dummy.get_mana(), 70)

    def test_if_current_stats_modifier_methods_work_correctly(self):
        
        with self.subTest("Test take_damage method."):
            self.dummy.take_damage(10)
            self.assertEqual(self.dummy.get_health(), 140)
        
        with self.subTest("Test take_mana method."):
            self.dummy.take_mana(10)
            self.assertEqual(self.dummy.get_mana(), 70)
        
        with self.subTest("Test take_health method."):
            self.dummy.take_healing(20)
            self.assertEqual(self.dummy.get_health(), 150)
    
    def test_can_cast_returns_true(self):
        self.assertTrue(self.dummy.can_cast())

if __name__ == "__main__":
    unittest.main()
