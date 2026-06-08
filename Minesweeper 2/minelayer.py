import random
import minefield
import tile

class Minelayer():

    initialSize = 0
    sizeSquared = initialSize * initialSize

    minesLaid = []

    def __init__(self, initialSize):

        self.initialSize = initialSize
        self.sizeSquared = initialSize * initialSize

    def layMines(self, clickedTile):

        i = 0
        self.minesLaid = []

        safeTiles = [clickedTile, clickedTile - (self.initialSize + 1), clickedTile - self.initialSize, clickedTile - (self.initialSize - 1), clickedTile - 1, clickedTile + 1, 
                     clickedTile + (self.initialSize - 1), clickedTile + self.initialSize, clickedTile + (self.initialSize + 1)]

        mf = minefield.Minefield(self.initialSize)

        while len(self.minesLaid) < self.sizeSquared / 5:
            
            if i % self.sizeSquared not in self.minesLaid and i % self.sizeSquared not in safeTiles:
                self.mine(mf.field[i % self.sizeSquared], i)

                if len(self.minesLaid) > self.sizeSquared / 5:
                    break

            i += 1

        for mine in range(self.sizeSquared):

            mf.field[mine].neighborBombs = mf.countBombs(mf.field, mine, self.initialSize)
        
        print("The mines are laid, good luck...")
        return mf

    def mine(self, tile, item):
        
        if random.randint(1,1000) < 11:
            tile.bomb = True
            #print("Laying mine at: ", item % self.sizeSquared)
            self.minesLaid.append(tile)
            #print("Mines laid: ", str(self.minesLaid))