import unittest
from hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.dummy = Hero(name="Bron", title="Dragonslayer", health=100,
                          mana=100, mana_regeneration_rate=2)

    def test_known_as_method(self):
        self.assertEqual(self.dummy.known_as(), 'Bron the Dragonslayer')


if __name__ == '__main__':
    unittest.main()
