
defaultFileDir = 'dungeon_maps/level_1/'
defaultMapFileName = 'map.txt'

class Dungeon:
    def __init__(self, *, fileDir=defaultFileDir):

        self.__fileName = ''
        self.open_map(fileDir= fileDir)

        self.__dungeonLayout = []
        self.__heroCoords = [0,0]
        
        self.__current_tile = '.'
    
    """
        Sets the fileName attribute to the passed in one. 
    """
    def open_map(self,*, fileDir= defaultFileDir):
        self.__fileName = fileDir + defaultMapFileName
        self.__get_dungeon_layout()

    """ 
        Extracts the dungeon map from the input file.
    """
    def __extract_dugeon_data(self, fileStream):
        for line in fileStream:
            self.__dungeonLayout.append(list(line.replace('\n', '')))
        
    """
        Reads the file containing a dungeon map and possibly several other things
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
        Returns the coordinates of the first spawn location found while iterating the map. 
    """
    def __find_spawn_location(self):
        for x in range(len(self.__dungeonLayout)):
            for y in range(len(self.__dungeonLayout[x])):
                if self.__dungeonLayout[x][y] == 'S':
                    return (x,y)
        
        return None
    
    """
        Overwrites the first spawn location found by the __find_spawn_location method.
    """
    def __overwrite_spawn_location(self):
        self.__dungeonLayout[self.__heroCoords[0]][self.__heroCoords[1]]= 'H'

    """
        Overwrites the first spawn location found with the H symbol. 
    """
    def spawn(self):
        
        locationCoords = self.__find_spawn_location()
        if locationCoords is not None:
            self.__heroCoords = list(locationCoords)
            self.__overwrite_spawn_location()
            return True

        return False

    """
        Checks if the hero will leave the map or hit an obstacle.
    """
    def __is_valid_move(self,stepX, stepY):        
        height = len(self.__dungeonLayout)
        width = len(self.__dungeonLayout[self.__heroCoords[0]])

        return ((self.__heroCoords[0] + stepX >= 0 and self.__heroCoords[0] + stepX < height)\
            and (self.__heroCoords[1] + stepY >= 0 and self.__heroCoords[1] + stepY < width)\
            and (self.__dungeonLayout[self.__heroCoords[0] + stepX][self.__heroCoords[1] + stepY] != '#'))

    """ 
        Returns the tile at given coordinates.
    """
    def __get_tile_at_coords(self,x,y):
        return self.__dungeonLayout[x][y]

    """
        Updates the tile at (x,y) with the given tile. 
    """
    def __update_tile(self,x,y,tile):
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
        
        
    """ 
        Moves the hero either up, down, left or right if possible.
    """
    def move_hero(self,*, direction):

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
            tile = self.__get_tile_at_coords(self.__heroCoords[0] + stepX, self.__heroCoords[1] + stepY)
            if tile == 'E':
                #initiate fight
                pass
            elif tile == 'T':
                #find treasure
                pass
            elif tile == 'G':
                #finish level
                pass
            else:
                self.__move(stepX, stepY,tile)
                pass
            return True
        
        return False

    def get_dungeon_layout(self):
        return self.__dungeonLayout
    
    def get_hero_coordinates(self):
        return self.__heroCoords