import unittest
from Entity import Entity


class EntityUnitTest(unittest.TestCase):
    def setUp(self):
        entities = Entity(name="Test", health=150, mana=70)

    def test_if_getters_work_correctly(self):
        self.assertEqual(entities.get_name(), "Test")
        self.assertEqual(entities.get_health(), 150)
        self.assertEqual(entities.get_mana(), 70)


if __name__ == "__main__":
    unittest.main()
