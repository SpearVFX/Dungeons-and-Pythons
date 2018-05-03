import json
import random


DEFAULT_TREASURE_FILE_NAME = 'treasures.json'


class Treasure:

    def __init__(self, *, fileDir):
        self.__fileDir = fileDir
        self.__elements = {}
        self.open_file(filePath=fileDir)
    
    ''' Loads the json file into the Treasure objects __elements attribute. '''
    
    def __get_elements(self, *, fullPath):
        with open(fullPath, 'r') as treasures:
            self.__elements = json.load(treasures)
    
    ''' Sets the current fileName to the passed in filePath + the default treasure file name. '''
    
    def open_file(self, *, filePath):
        fullPath = filePath + DEFAULT_TREASURE_FILE_NAME
        self.__get_elements(fullPath=fullPath)

    ''' Returns a single item from the treasure.json file.'''
    
    def pick_one(self):

        dice = random.randint(0, len(self.__elements))

        if dice == len(self.__elements):
            return None

        lootPool = list(self.__elements)[dice]
        poolType = lootPool

        dice = random.randint(0, len(self.__elements[lootPool]) - 1)
        return (poolType, self.__elements[lootPool][dice])
