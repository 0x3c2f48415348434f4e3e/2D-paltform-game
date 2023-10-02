#Here is the file we will use to do everything for out map
from gameSetup import setup
import numpy
import os

class initMap(setup):
    def __init__(self) -> None:
        super().__init__()
        self.mapData = numpy.zeros((self.mapWidth,self.mapHeight), dtype=list)
    
    def loadTiles(self,filename):
        '''Since we only have a single tile type, we
        we can just open just that file
        '''
        try:
            #make tile accessible throughout (do later)
            tile = open(filename, 'r') #This is for tile
        except FileExistsError as e:
            print(e)
    
    def loadMap(self, dataFile):
        '''Now remeber above we set all the index of our
           map data to be 0. Now here what we want to do
           is to loop through our 'dataFile' and then assign
           the correspong value to the 2D array map
        '''
        
        #note in our map data, 0 means nothing and 1 means tile
        '''
        So what we want to do is open our file, and read each chracter
        '''
        dataInfo = open(dataFile, 'r')
        for i in range(self.mapHeight):
            #start from verticle and go across
            for j in range(self.mapWidth):
                char = dataInfo.read(1)
                self.mapData[j][i] = char
test = initMap()
test.loadTiles(f"{os.getcwd()}/static/tile.png")
test.loadMap(f"{os.getcwd()}/data/map1.dat")
print(test.mapData[0][0])