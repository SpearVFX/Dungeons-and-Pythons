from src.treasure import Treasure
from src.weapon import Weapon
from src.spell import Spell
from src.hero import Hero
from src.enemy import Enemy
from src.fight import Fight
from src.fight_status_bar import FightStatusBar

import sys
import os.path
import csv
import pdb


DEFAULT_FILE_DIR = 'dungeon_maps/level_1/'
DEFAULT_MAP_FILE_NAME = 'map.txt'
DEFAULT_ENEMY_FILE_NAME = 'enemies.csv'

DEFAULT_TILE = '.'
ENEMY_TILE = 'E'
TREASURE_TILE = 'T'
GATEWAY_TILE = 'G'
SPAWN_TILE = 'S'
HERO_TILE = 'H'
WALL_TILE = '#'


class Dungeon:
    def __init__(self, *, fileDir=DEFAULT_FILE_DIR):

        
        self.__fileDir = fileDir
        self.__dungeonLayout = []

        self.open_map(fileDir=fileDir)
        self.__treasure = Treasure(fileDir=fileDir)

        self.__enemies = []
        self.__extract_enemies()

        self.__hero = None
        self.__currEnemy=None
    
    """ 
        Sets the fileName attribute to the passed in one.
    """

    def open_map(self, *, fileDir=DEFAULT_FILE_DIR):
        fileName = fileDir + DEFAULT_MAP_FILE_NAME
        
        self.__get_dungeon_layout(fullPath=fileName)
        
        self.__fileDir = fileDir
        self.__extract_enemies()


    """
        Reads the file containing a dungeon map
        and possibly several other things
        and stores in into the dungeonLayout attribute.
    """

    def __get_dungeon_layout(self,*,fullPath):
        self.__dungeonLayout = []
        with open(fullPath, 'r') as file:
            self.__extract_dugeon_data(file)

    """
        Extracts the dungeon map from the input file.
    """

    def __extract_dugeon_data(self, fileStream):
        for line in fileStream:
            self.__dungeonLayout.append(list(line.replace('\n', '')))

    """
        Extracts the enemeis from the enemies.csv file. 
    """

    def __extract_enemies(self):
        self.__enemies =[]
        fullPath = self.__fileDir + DEFAULT_ENEMY_FILE_NAME
        
        if os.path.exists(fullPath): 
            with open(fullPath, 'r') as f:
                for line in csv.reader(f):
                    self.__enemies.append(Enemy(name=line[0],
                                                health=int(line[1]),
                                                mana=int(line[2]),
                                                damage=int(line[3])))
        
    """
        Print the symbol to the console window.
    """

    def __print_colorized(self, symbol):
        
        if symbol == 'S' or symbol == 'H':
            print(f'\x1b[28m{symbol}\x1b[0m', end='', flush=True)
        elif symbol == 'G':
            print(f'\x1b[36m{symbol}\x1b[0m', end='', flush=True)
        elif symbol == '#':
            print(f'\x1b[37m{symbol}\x1b[0m', end='', flush=True)
        elif symbol == '.':
            print(f'\x1b[30m{symbol}\x1b[0m', end='', flush=True)
        elif symbol == 'T':
            print(f'\x1b[33m{symbol}\x1b[0m', end='', flush=True)
        elif symbol == 'E':
            print(f'\x1b[31m{symbol}\x1b[0m', end='', flush=True)
        else:
            print(symbol, end='', flush=True)
        pass

    def print_map(self):
        for row in range(len(self.__dungeonLayout)):
            for col in range(len(self.__dungeonLayout[row])):
                if (col, row) == self.__hero.get_coords():
                    self.__print_colorized(HERO_TILE)
                elif (col,row) == self.__currEnemy.get_coords():
                    self.__print_colorized(ENEMY_TILE)

                else:
                    self.__print_colorized(self.__dungeonLayout[row][col])
            print()

    """
        Returns the coordinates of the first spawn
        location found while iterating the map.
    """

    def __find_spawn_location(self):
        for x in range(len(self.__dungeonLayout)):
            for y in range(len(self.__dungeonLayout[x])):
                if self.__dungeonLayout[x][y] == SPAWN_TILE:
                    return (x, y)

        return None

    """
        Overwrites the first spawn location found with the DEFAULT_TILE symbol.
    """

    def spawn(self, *, hero):

        locationCoords = self.__find_spawn_location()
        if locationCoords is not None:
            self.__hero = hero
            self.__hero.set_coords(x = locationCoords[0], y = locationCoords[1])
            self.__update_tile(x=locationCoords[0],y=locationCoords[1],tile=DEFAULT_TILE)
            return True

        return False

    """
        Checks if the passed in coordinates x and y are valid. 
    """

    def __are_valid_coords(self,*, x, y):
        height = len(self.__dungeonLayout)
        width = len(self.__dungeonLayout[0])

        return (x >= 0 and x < width) and (y >= 0 and y < height)


    """
        Checks if the hero will leave the map or hit an obstacle.
    """

    def __is_valid_move(self,*,target, stepX, stepY):
        coords = target.get_coords()
        
        nX = coords[0] + stepX
        nY = coords[1] + stepY
        
        return (
                self.__are_valid_coords(x=nX,y=nY) and
                (self.__dungeonLayout[nY][nX] != WALL_TILE)
               )

    """
        Returns the tile at given coordinates.
    """

    def __get_tile_at_coords(self, x, y):
        return self.__dungeonLayout[y][x]

    """
        Updates the tile at (x,y) with the given tile.
    """

    def __update_tile(self,*, x, y, tile):
        self.__dungeonLayout[y][x] = tile

    """
        This will move the character to the requessted direction
        saving the tile that will be overriden.
    """

    def __move(self, *,target, x, y):
        if(self.__hero.is_alive()):
            coords = target.get_coords()   
            target.set_coords(x = coords[0] + x, y = coords[0] + y)


    """
        Asks the player if he wants to update his arsenal with the passed in item. 
    """

    def __prompt_arsenal_update(self, item):
        print(item)
        command = input(f'Would you like to change your current arsenal?:\
                        \n{self.__hero.get_weapon()}\
                        \n{self.__hero.get_spell()}\
                        \n Input Y or N:')

        if command is 'Y':
            return True

        return False

    """
        Pick's a treasure from the treasure file and does something according to what the treasure is.
    """
    
    def __loot_treasure(self):
        item = self.__treasure.pick_one()

        if item is None:
            print('The chest was empty.')
            return

        print(f'You\'ve looted a {item[0]}.\n')

        if item[0] == 'potion':
            if(item[1]['name'] == 'Mana'):
                self.__hero.take_mana(item[1]['amount'])
            else:
                self.__hero.take_healing(item[1]['amount'])

        else:
            command = (self.__prompt_arsenal_update(item))
            if command:
                if item[0] == 'weapon':

                    weapon = Weapon(name=item[1]['name'],
                                    damage=item[1]['damage'])
                    self.__hero.equip(weapon)

                elif item[0] == 'spell':
                    spell = Spell(name=item[1]['name'],
                                  damage=item[1]['damage'],
                                  manaCost=item[1]['manaCost'],
                                  castRange=item[1]['range'])
                    self.__hero.learn(spell)

    """
        Generates the name of the dir containing the next level.
    """

    def __generate_next_level_dir_name(self):
        length = len(DEFAULT_FILE_DIR)-2
        levelIndex = str(int(self.__fileDir[length:][:-1]) + 1)
        nextLevelDirName = (self.__fileDir[0:length]) + levelIndex + '/'
        return nextLevelDirName

    """
        Loads the next level if there is one.
    """

    def __load_next_level(self):
        nextLevelDirName = self.__generate_next_level_dir_name()

        if os.path.exists(nextLevelDirName):
            self.open_map(fileDir=nextLevelDirName)
            self.__treasure.open_file(filePath=nextLevelDirName)
            return True

        return False

    """
        Checks each tile along the spell range. 
    """

    def __get_enemy_coords_in_range(self, *,castRange):
        hero_coords = self.__hero.get_coords()

        for i in range(1,castRange+1):
            if  self.__are_valid_coords(x=hero_coords[0] + i,y=hero_coords[0]):

                if self.__get_tile_at_coords(hero_coords[0] + i, hero_coords[0]) == '#':
                    break  

                elif self.__get_tile_at_coords(hero_coords[0] + i, hero_coords[0]) == 'E':
                    return (hero_coords[0] +i, hero_coords[0])
            else:
                break

        for i in range(1, castRange+1):
            if self.__are_valid_coords(x=hero_coords[0], y=hero_coords[0] + i):
                
                if self.__get_tile_at_coords(hero_coords[0], hero_coords[0] + i) == '#':
                    break
            
                elif self.__get_tile_at_coords(hero_coords[0], hero_coords[0] +i)== 'E':
                    return (hero_coords[0], hero_coords[0] + i)
            else:
                break

        return None

    """
        Checks if there's an enemy in the heroes spell attack range.
    """
    
    def __check_for_enemies_in_range(self):
        
        spellRange = self.__hero.get_spell().get_castRange()
        enemyCoords= self.__get_enemy_coords_in_range(castRange=spellRange)
    
        if enemyCoords != None:
            return enemyCoords

        return None
    

    """
        Starts a fight with an enemy at given coords. 
    """

    def start_fight(self,*, enemyX, enemyY):
        self.__currEnemy = self.__enemies.pop()
        self.__currEnemy.set_coords(x=enemyX, y=enemyY)
        fight = Fight(hero=self.__hero, enemy=self.__currEnemy, dungeon=self)
                
        fight.initialize_fight()

        self.update_map_by_results(fight= fight,
                                   initialEnemyCoords=(enemyX,enemyY),
                                   currEnemyCoords=self.__currEnemy.get_coords())
    

    """
        Updates the map depending on who won the fight. 
    """

    def update_map_by_results(self, fight, initialEnemyCoords, currEnemyCoords):
        winner = fight.get_winner()
        
        self.__update_tile(x=currEnemyCoords[0],
                           y=currEnemyCoords[1],
                           tile=DEFAULT_TILE)
        if type(winner) is Enemy:
            self.__update_tile(x=initialEnemyCoords[0],
                               y=initialEnemyCoords[1],
                               tile=ENEMY_TILE)

            winner.heal_to_full()
            self.__enemies.append(winner)

            self.__hero.set_coords(x=None, y=None)
                
            

    """
        Initiate a fight with an enemy if there's one in range.
    """

    def shoot_blindly(self):
        if self.__hero.can_cast():
            coords = self.__check_for_enemies_in_range()

            if coords != None:
                self.__update_tile(x=coords[0],
                                   y=coords[1],
                                   tile=DEFAULT_TILE)
                                   
                self.start_fight(enemyX=coords[0],
                                 enemyY=coords[1])
                return True

            else:
                print("No enemies within spell range.")

        return False

    """
        Moves the hero either up, down, left or right if possible.
    """

    def move_hero(self, *, direction):

        stepX = 0
        stepY = 0

        if direction == 'up':
            stepY = -1
        elif direction == 'down':
            stepY = 1
        elif direction == 'left':
            stepX = -1
        elif direction == 'right':
            stepX = 1

        coords = self.__hero.get_coords()

        if(self.__is_valid_move(target=self.__hero,
                                stepX=stepX,
                                stepY=stepY)):
            
            tile = self.__get_tile_at_coords(coords[0] + stepX,
                                             coords[1] + stepY)
            

            if tile == ENEMY_TILE:
                self.start_fight(enemyX=coords[0]+stepX,
                                 enemyY=coords[1]+stepY)
            
            elif tile == TREASURE_TILE:
                self.__loot_treasure()
                self.__update_tile(x=coords[0]+stepX,
                                   y=coords[1]+stepY,
                                   tile=DEFAULT_TILE)

            elif tile == GATEWAY_TILE:
                if self.__load_next_level():
                    self.spawn(hero=self.__hero)
                else:
                    return self.credits()

            self.__move(target=self.__hero,
                        x=stepX,
                        y=stepY)
            return True

        return False
    

    """
        Sets one of the coordinates of the chaser a tile closer to the chased target.
    """

    def chase(self,*,chaser, chased):
        chaserCoords = chaser.get_coords()
        chasedCoords = chased.get_coords()

        distance = 0

        if chaserCoords[0] != chasedCoords[0]:
            distance = (chasedCoords[0]-chaserCoords[0])
            stepX = distance//abs(distance)
            if self.__is_valid_move(target=chaser, stepX=stepX, stepY=chaserCoords[1]):
                chaser.set_coords(x=chaserCoords[0] + stepX,y=chaserCoords[1])
                return
                

        if chaserCoords[1] != chasedCoords[1]:
            distance = (chasedCoords[1]-chaserCoords[1])
            stepY = distance//abs(distance)
            if self.__is_valid_move(target=chaser, stepX=chaserCoords[0], stepY=stepY):
                chaser.set_coords(x=chaserCoords[0],y=chaserCoords[1] + stepY)
                
        
    def get_dungeon_layout(self):
        return self.__dungeonLayout

    def get_hero_coordinates(self):
        return self.__hero.get_coords()

    def get_hero(self):
        return self.__hero

    def credits(self):
        return "Congratulations, You've finied the game!\
                Directed and written by:\n\
                Sasho Kostov and Dimitar Lukanov."
