import json
import random


defaultTreasureFileName = 'treasures.json'

class Treasure:
    
    def __init__(self, *, filePath):
        self.__fileName = filePath
        self.__elements = {}
    
    def __get_elements(self):
        self.__elements = json.load(self.__fileName)

    def open_file(self, *, filePath):
        self.__filePath = filePath + defaultTreasureFileName
        self.__get_elements()

    def pick_one(self):
        
        dice = random.randint(0,len(self.__elements))
        
        if dice == len(self.__elements):
            return None
        
        lootPool = list(self.__elements)[dice]

        dice = random.randint(0,len(lootPool)-1)
        
        return lootPool[dice]



    

    
