import unittest

from dungeon import Dungeon


validMapName = 'dungeon_maps/level1.txt'
class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.dummy = Dungeon(fileName = validMapName)

    def test_spawn_method(self):
        self.dummy.spawn()
        self.assertEqual(
            self.dummy.get_dungeon_layout()[self.dummy.get_hero_coordinates()[0]]\
                                            [self.dummy.get_hero_coordinates()[1]],
            'H'
        )


if __name__ == '__main__':
    unittest.main()