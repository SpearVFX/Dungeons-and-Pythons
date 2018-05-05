from src.treasure import Treasure
from src.weapon import Weapon
from src.spell import Spell
from src.hero import Hero
from src.enemy import Enemy
from src.fight import Fight
from src.fight_status_bar import FightStatusBar
import src.hero
import sys
import os.path


DEFAULT_FILE_DIR = 'dungeon_maps/level_1/'
DEFAULT_MAP_FILE_NAME = 'map.txt'

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

        self.__hero = None

        self.__current_tile = DEFAULT_TILE

    """ 
        Sets the fileName attribute to the passed in one.
    """

    def open_map(self, *, fileDir=DEFAULT_FILE_DIR):
        fileName = fileDir + DEFAULT_MAP_FILE_NAME
        self.__get_dungeon_layout(fullPath=fileName)
        self.__fileDir = fileDir

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
        Print the map to the console window.
    """

    def print_map(self):
        for row in self.__dungeonLayout:
            print(''.join(row))

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
        Overwrites the first spawn location found
        by the __find_spawn_location method.
    """

    def __overwrite_spawn_location(self, *,coordinates):
        self.__hero.set_coords(x = coordinates[0], y = coordinates[1])
        heroCoords = self.__hero.get_coords()
        self.__dungeonLayout[heroCoords[0]][heroCoords[1]] = HERO_TILE

    """
        Overwrites the first spawn location found with the H symbol.
    """

    def spawn(self, *, hero):

        locationCoords = self.__find_spawn_location()
        if locationCoords is not None:
            self.__hero = hero
            self.__overwrite_spawn_location(coordinates = locationCoords)
            return True

        return False

    """
        Checks if the passed in coordinates x and y are valid. 
    """

    def __are_valid_coords(self, x, y):
        height = len(self.__dungeonLayout)
        width = len(self.__dungeonLayout[0])

        return (x >= 0 and x < width) and (y >= 0 and y < height)


    """
        Checks if the hero will leave the map or hit an obstacle.
    """

    def __is_valid_move(self, stepX, stepY):
        coords = self.__hero.get_coords()
        
        nX = coords[0] + stepX
        nY = coords[1] + stepY

        return (
                self.__are_valid_coords(nX,nY) and
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

    def __move(self, x, y, tile):
        coords = self.__hero.get_coords()
        
        self.__update_tile(x=coords[0],
                           y=coords[1],
                           tile= self.__current_tile)

        self.__current_tile = tile

        self.__hero.set_coords(x = coords[0] + x, y = coords[0] + y)

        coords = self.__hero.get_coords()

        self.__update_tile(x=coords[0],
                           y=coords[1],
                           tile=HERO_TILE)

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
            if  self.__are_valid_coords(hero_coords[0] + i, hero_coords[0]):

                if self.__get_tile_at_coords(hero_coords[0] + i, hero_coords[0]) == '#':
                    break  

                elif self.__get_tile_at_coords(hero_coords[0] + i, hero_coords[0]) == 'E':
                    return (hero_coords[0] +i, hero_coords[0])
            else:
                break

        for i in range(1, castRange+1):
            if self.__are_valid_coords(hero_coords[0], hero_coords[0] + i):
                
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
        
        if self.__hero.get_spell() != None:
        
            spellRange = self.__hero.get_spell().get_castRange()
            enemyCoords= self.__get_enemy_coords_in_range(castRange=spellRange)
        
            if enemyCoords != None:
                return enemyCoords

        return None
    

    """
        Starts a fight with an enemy at given coords. 
    """

    def start_fight(self, enemyCoords):
        enemy = Enemy()
        enemy.set_coords(x=enemyCoords[0], y=enemyCoords[1])

        fight = Fight(hero=self.__hero, enemy=enemy)
        fight.initialize_fight()
        
        self.update_map_by_results(fight= fight,enemyCoords= enemyCoords)
    

    """
        Updates the map depending on who won the fight. 
    """

    def update_map_by_results(self, fight, enemyCoords):
        winner = fight.get_winner()
        if type(winner) is Hero:
            self.__hero.set_coords(enemyCoords[0], enemyCoords[1])

        elif type(winner) is Enemy:
            self.__update_tile(x=enemyCoords[0],
                               y=enemyCoords[1],
                               tile=ENEMY_TILE)

            heroCoords = self.__hero.get_coords()

            self.__update_tile(x=heroCoords[0],
                               y=heroCoords[1],
                               tile=DEFAULT_TILE)    

            self.__hero.__set_coords(x=None, y=None)

    """
        Initiate a fight with an enemy if there's one in range.
    """

    def shoot_blindly(self):
        if self.__hero.can_cast():
            coords = self.__check_for_enemies_in_range()

            if coords != None:
                self.start_fight(coords)
        else:
            print('Not enough mana!')
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

        if(self.__is_valid_move(stepX, stepY)):
            tile = self.__get_tile_at_coords(
                coords[0] + stepX,
                coords[1] + stepY)
            
            if tile == ENEMY_TILE:
                # initiate fight
                pass
            
            elif tile == TREASURE_TILE:
                self.__loot_treasure()
                tile = DEFAULT_TILE
            
            elif tile == GATEWAY_TILE:
                if self.__load_next_level():
                    self.spawn(hero=self.__hero)
                else:
                    return self.credits()

            self.__move(stepX, stepY, tile)
            return True

        return False

    def credits(self):
        return "Congratulations, You've finied the game!\
                Directed and written by:\n\
                Sasho Kostov and Dimitar Lukanov."

    def get_dungeon_layout(self):
        return self.__dungeonLayout

    def get_hero_coordinates(self):
        return self.__hero.get_coords()

    def get_hero(self):
        return self.__hero
