import unittest

from dungeon import Dungeon


plainMapDir = 'dungeon_maps/test_maps/plain_map/'
validMapDir = 'dungeon_maps/level_1/'

class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.dummy = Dungeon()
        #self.dummy.print_map()

    def test_spawn_method(self):
        self.dummy.open_map(fileDir = plainMapDir)
        self.dummy.spawn()
        #self.dummy.print_map()
        self.assertEqual(
            self.dummy.get_dungeon_layout()[self.dummy.get_hero_coordinates()[0]]\
                                            [self.dummy.get_hero_coordinates()[1]],
            'H'
        )

    def test_move_method(self):
        
        with self.subTest('Test moving up.'):
            self.dummy.open_map(fileDir = plainMapDir)
            self.dummy.spawn()
            self.dummy.move_hero(direction = 'up')
            
            self.assertAlmostEqual(
                self.dummy.get_dungeon_layout()[0][1],
                'H'
            )

        with self.subTest('Test moving down.'):
            self.dummy.open_map(fileDir = plainMapDir)
            self.dummy.spawn()
            self.dummy.move_hero(direction = 'down')
            
            self.assertAlmostEqual(
                self.dummy.get_dungeon_layout()[2][1],
                'H'
            )

        with self.subTest('Test moving right.'):
            self.dummy.open_map(fileDir = plainMapDir)
            self.dummy.spawn()
            self.dummy.move_hero(direction = 'right')

            self.assertAlmostEqual(
                self.dummy.get_dungeon_layout()[1][2],
                'H'
            )
        with self.subTest('Test moving left.'):
            self.dummy.open_map(fileDir = plainMapDir)
            self.dummy.spawn()
            self.dummy.move_hero(direction = 'left')

            self.assertAlmostEqual(
                self.dummy.get_dungeon_layout()[1][0],
                'H'
            )


if __name__ == '__main__':
    unittest.main()