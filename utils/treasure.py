import json
import random


defaultTreasureFileName = 'treasures.json'

class Treasure:
    
    def __init__(self, *, filePath):
        self.__fileName = filePath + defaultTreasureFileName
        self.__elements = {}
        self.__get_elements()
    
    def __get_elements(self):
        with open(self.__fileName,'r') as treasures:
            self.__elements = json.load(treasures)

    def open_file(self, *, filePath):
        self.__fileName = filePath + defaultTreasureFileName
        self.__get_elements()

    def pick_one(self):
        
        dice = random.randint(0,len(self.__elements))
        
        if dice == len(self.__elements):
            return None
                
        lootPool = list(self.__elements)[dice]
        poolType = lootPool
        
        dice = random.randint(0,len(self.__elements[lootPool])-1)
        return (poolType, self.__elements[lootPool][dice])




    

    
