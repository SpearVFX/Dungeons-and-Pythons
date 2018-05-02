import unittest

from enemy import Enemy


class EnemyTests(unittest.TestCase):
    def setUp(self):
        self.dummy = Enemy(health=100, mana=100, damage=20)

    def test_get_base_damage_method(self):
        self.assertEqual(self.dummy.get_base_damage(), 20)


if __name__ == '__main__':
    unittest.main()
