from treasure import Treasure
from weapon import Weapon
from spell import Spell
import hero
import pdb

DEFAULT_FILE_DIR = 'dungeon_maps/level_1/'
DEFAULT_MAP_FILE_NAME = 'map.txt'
DEFAULT_TILE = '.'


class Dungeon:
    def __init__(self, *, fileDir=DEFAULT_FILE_DIR):

        self.__fileName = ''
        self.__dungeonLayout = []

        self.open_map(fileDir=fileDir)
        self.__treasure = Treasure(filePath=fileDir)

        self.__hero = None
        self.__heroCoords = [0, 0]
        self.__current_tile = DEFAULT_TILE

    """
        Sets the fileName attribute to the passed in one.
    """

    def open_map(self, *, fileDir=DEFAULT_FILE_DIR):
        self.__fileName = fileDir + DEFAULT_MAP_FILE_NAME
        self.__get_dungeon_layout()

    """
        Extracts the dungeon map from the input file.
    """

    def __extract_dugeon_data(self, fileStream):
        for line in fileStream:
            self.__dungeonLayout.append(list(line.replace('\n', '')))

    """
        Reads the file containing a dungeon map
        and possibly several other things
        and stores in into the dungeonLayout attribute.
    """

    def __get_dungeon_layout(self):
        self.__dungeonLayout = []
        with open(self.__fileName, 'r') as file:
            self.__extract_dugeon_data(file)

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
                if self.__dungeonLayout[x][y] == 'S':
                    return (x, y)

        return None

    """
        Overwrites the first spawn location found
        by the __find_spawn_location method.
    """

    def __overwrite_spawn_location(self):
        self.__dungeonLayout[self.__heroCoords[0]][self.__heroCoords[1]] = 'H'

    """
        Overwrites the first spawn location found with the H symbol.
    """

    def spawn(self, *, hero):

        locationCoords = self.__find_spawn_location()
        if locationCoords is not None:
            self.__hero = hero
            self.__heroCoords = list(locationCoords)
            self.__overwrite_spawn_location()
            return True

        return False

    """
        Checks if the hero will leave the map or hit an obstacle.
    """

    def __is_valid_move(self, stepX, stepY):
        height = len(self.__dungeonLayout)
        width = len(self.__dungeonLayout[self.__heroCoords[0]])

        nX = self.__heroCoords[0] + stepX
        nY = self.__heroCoords[1] + stepY
        return ((self.__heroCoords[0] + stepX >= 0 and
                 self.__heroCoords[0] + stepX < height) and
                (self.__heroCoords[1] + stepY >= 0 and
                 self.__heroCoords[1] + stepY < width) and
                (self.__dungeonLayout[nX][nY] != '#'))

    """
        Returns the tile at given coordinates.
    """

    def __get_tile_at_coords(self, x, y):
        return self.__dungeonLayout[x][y]

    """
        Updates the tile at (x,y) with the given tile.
    """

    def __update_tile(self, x, y, tile):
        self.__dungeonLayout[x][y] = tile

    """
        This will move the character to the requessted direction
        saving the tile that will be overriden.
    """

    def __move(self, x, y, tile):
        self.__update_tile(self.__heroCoords[0],
                           self.__heroCoords[1],
                           self.__current_tile)

        self.__current_tile = tile

        self.__heroCoords[0] += x
        self.__heroCoords[1] += y

        self.__update_tile(self.__heroCoords[0],
                           self.__heroCoords[1],
                           'H')

    def __promt_arsenal_update(self, item):
        print(item)
        command = input(f'Would you like to change your current arsenal?:\
                        \n{self.__hero.get_weapon()}\
                        \n{self.__hero.get_spell()}\
                        \n Input Y or N:')
        if command is 'Y':
            return True

        return False

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
            command = (self.__promt_arsenal_update(item))
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
        Moves the hero either up, down, left or right if possible.
    """

    def move_hero(self, *, direction):

        stepX = 0
        stepY = 0

        if direction == 'up':
            stepX = -1
        elif direction == 'down':
            stepX = 1
        elif direction == 'left':
            stepY = -1
        elif direction == 'right':
            stepY = 1

        if(self.__is_valid_move(stepX, stepY)):
            tile = self.__get_tile_at_coords(
                self.__heroCoords[0] + stepX,
                self.__heroCoords[1] + stepY)
            if tile == 'E':
                # initiate fight
                pass
            elif tile == 'T':
                self.__loot_treasure()
                tile = DEFAULT_TILE
            elif tile == 'G':
                # finish level
                pass

            self.__move(stepX, stepY, tile)
            pass
            return True

        return False

    def get_dungeon_layout(self):
        return self.__dungeonLayout

    def get_hero_coordinates(self):
        return self.__heroCoords

    def get_hero(self):
        return self.__hero
