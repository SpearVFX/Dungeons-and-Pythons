import unittest
from src.dungeon import Dungeon
from src.hero import Hero
from src.spell import Spell
import pdb

plainMapDir = 'dungeon_maps/test_maps/plain_map/'
treasureMapDir='dungeon_maps/test_maps/treasure_map/'
enemyMapDir='dungeon_maps/test_maps/enemy_map/'
validMapDir = 'dungeon_maps/level_1/'


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.dummy = Dungeon()
        self.hero = Hero(name='Fuggboi',title='Wise')

    def test_spawn_method(self):
        self.dummy.open_map(fileDir=plainMapDir)
        self.dummy.spawn(hero=self.hero)
        # self.dummy.print_map()
        self.assertEqual(
                self.hero.get_coords(),
                (1,1))

    def test_move_method(self):

        with self.subTest('Test moving up.'):
            self.dummy.open_map(fileDir=plainMapDir)
            self.dummy.spawn(hero=self.hero)
            self.dummy.move_hero(direction='up')
            self.assertEqual(
                self.hero.get_coords(),
                (1,0)
            )

        with self.subTest('Test moving down.'):
            self.dummy.open_map(fileDir=plainMapDir)
            self.dummy.spawn(hero=self.hero)
            self.dummy.move_hero(direction='down')
            self.assertEqual(
                self.hero.get_coords(),
                (1,2)
            )

        with self.subTest('Test moving right.'):
            self.dummy.open_map(fileDir=plainMapDir)
            self.dummy.spawn(hero=self.hero)
            self.dummy.move_hero(direction='right')

            self.assertEqual(
                self.hero.get_coords(),
                (2,1)
            )

        with self.subTest('Test moving left.'):
            self.dummy.open_map(fileDir=plainMapDir)
            self.dummy.spawn(hero=self.hero)
            self.dummy.move_hero(direction='left')

            self.assertEqual(
                self.hero.get_coords(),
                (0,1)
            )

        with self.subTest('Test moving into treasure chest.'):
            self.dummy.open_map(fileDir=treasureMapDir)
            self.dummy.spawn(hero=self.hero)

        with self.subTest('Test moving into enemy.'):
            self.dummy.open_map(fileDir=enemyMapDir)
            self.dummy.spawn(hero=self.hero)
            self.dummy.move_hero(direction='right')
        
        with self.subTest('Test shoot_blindly method.'):
            self.hero.heal_to_full()
            self.dummy.open_map(fileDir=enemyMapDir)
            s1 = Spell(name="Magic spit", damage=30, manaCost=25, castRange=2)
            self.hero.learn(s1)
            self.dummy.spawn(hero=self.hero)
            self.dummy.shoot_blindly()
            self.dummy.print_map()

        with self.subTest('Test moving into gateway.'):
            self.dummy.open_map(fileDir=validMapDir)
            self.dummy.spawn(hero=self.hero)
            self.assertEqual(self.dummy.move_hero(direction='right'), True)
        
        with self.subTest('Test moving into gateway work when dirs have larger indexes.'):
            temp = 'dungeon_maps/level_99/'
            self.dummy.open_map(fileDir=temp)
            self.dummy.spawn(hero=self.hero)
            self.assertEqual(type(self.dummy.move_hero(direction='right')),str)
        
if __name__ == '__main__':
    unittest.main()
