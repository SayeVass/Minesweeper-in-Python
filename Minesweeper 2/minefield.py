import tile

class Minefield():

    depth = 0

    size = 0
    sizeSquared = size * size

    def __init__(self, size):

        self.size = size
        self.field = [tile.Tile() for i in range(size * size)]
    
    def countBombs(self, gameField, tileNumber, size):

        match self.checkCondition(gameField, tileNumber, size):
            case "tl":
                return self.checkCorner(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "tr":
                return self.checkCorner(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "bl":
                return self.checkCorner(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "br":
                return self.checkCorner(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "top":
                return self.checkWall(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "btm":
                return self.checkWall(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "lft":
                return self.checkWall(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "rgt":
                return self.checkWall(gameField, tileNumber, size, self.checkCondition(gameField, tileNumber, size))
            case "full":
                return self.checkFull(gameField, tileNumber, size)
    
    def checkCondition(self, gameField, tileNumber, size):

        # Special conditionting to check for neightbor bombs in corners of the gameboard
        if tileNumber == 0:

            return "tl"

        if tileNumber == size - 1:

            return "tr"
        
        if tileNumber == (size * size) - size:

            return "bl"

        if tileNumber == (size * size) - 1:

            return "br"

        # Special conditioning to check for neighbor bombs along walls of the gameboard
        if tileNumber < size:

            return "top"

        if tileNumber // size == size - 1:

            return "btm"

        if tileNumber % size == 0:

            return "lft"

        if tileNumber % size == size - 1:

            return "rgt"

        return "full"

    def checkCorner(self, gameField, tileNumber, size, pos):

        count = 0

        if pos == "tl":
            if self.checkForBomb(gameField, tileNumber + 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + size):
                count += 1
            if self.checkForBomb(gameField, tileNumber + size + 1):
                count += 1

            return count

        if pos == "tr":
            if self.checkForBomb(gameField, tileNumber - 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + (size - 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber + size):
                count += 1

            return count
        
        if pos == "bl":
            if self.checkForBomb(gameField, tileNumber - size):
                count += 1
            if self.checkForBomb(gameField, tileNumber - (size - 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber + 1):
                count += 1

            return count

        if pos == "br":
            if self.checkForBomb(gameField, tileNumber - (size + 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber - size):
                count += 1
            if self.checkForBomb(gameField, tileNumber - 1):
                count += 1

            return count

    def checkWall(self, gameField, tileNumber, size, pos):

        count = 0

        if pos == "top":
            if self.checkForBomb(gameField, tileNumber - 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + (size - 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber + size):
                count += 1
            if self.checkForBomb(gameField, tileNumber + (size + 1)):
                count += 1

            return count

        if pos == "btm":
            if self.checkForBomb(gameField, tileNumber - (size + 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber - size):
                count += 1
            if self.checkForBomb(gameField, tileNumber - (size - 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber - 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + 1):
                count += 1

            return count

        if pos == "lft":
            if self.checkForBomb(gameField, tileNumber - size):
                count += 1
            if self.checkForBomb(gameField, tileNumber - (size - 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber + 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + size):
                count += 1
            if self.checkForBomb(gameField, tileNumber + (size + 1)):
                count += 1

            return count

        if pos == "rgt":
            if self.checkForBomb(gameField, tileNumber - (size + 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber - size):
                count += 1
            if self.checkForBomb(gameField, tileNumber - 1):
                count += 1
            if self.checkForBomb(gameField, tileNumber + (size - 1)):
                count += 1
            if self.checkForBomb(gameField, tileNumber + size):
                count += 1

            return count

    def checkFull(self, gameField, tileNumber, size):

        count = 0

        if self.checkForBomb(gameField, tileNumber - (size + 1)):
            count += 1
        if self.checkForBomb(gameField, tileNumber - size):
            count += 1
        if self.checkForBomb(gameField, tileNumber - (size - 1)):
            count += 1
        if self.checkForBomb(gameField, tileNumber - 1):
            count += 1
        if self.checkForBomb(gameField, tileNumber + 1):
            count += 1
        if self.checkForBomb(gameField, tileNumber + (size - 1)):
            count += 1
        if self.checkForBomb(gameField, tileNumber + size):
            count += 1
        if self.checkForBomb(gameField, tileNumber + (size + 1)):
            count += 1

        return count

    def checkForBomb(self, gameField, checkTile):
        #print("Checking for bomb at ", checkTile)

        if gameField[checkTile].bomb:
            #print("Bomb found")
            return True
        else:
            return False

    def checkForZeros(self, gameField, tileNumber, size, checkList):

        tileList = []
        
        #print("checking for 0s in ", end="")

        for item in checkList:

            adjTiles = [
                item - (size + 1), #0 top left corner
                item - size,       #1 top middile
                item - (size - 1), #2 top right corner
                item - 1,          #3 left of item
                item + 1,          #4 right of item
                item + (size - 1), #5 bottom left corner
                item + size,       #6 bottom middle
                item + (size + 1)] #7 bottom right corner

            match len(self.checkCondition(gameField, item, size)):
                case 2:

                    cornerList = self.checkZerosCorner(gameField, adjTiles, self.checkCondition(gameField, item, size))

                    for cornerTile in cornerList:
                        if cornerTile not in tileList:
                            tileList.append(cornerTile)
                            if gameField[cornerTile].neighborBombs == 0:
                                checkList.append(cornerTile)
                        
                case 3:

                    wallList = self.checkZerosWall(gameField, adjTiles, self.checkCondition(gameField, item, size))

                    for wallTile in wallList:
                        if wallTile not in tileList:
                            tileList.append(wallTile)
                            if gameField[wallTile].neighborBombs == 0:
                                checkList.append(wallTile)
            
                case 4:
                    #print("open space")

                    for openTile in adjTiles:
                        if openTile not in tileList:
                            tileList.append(openTile)
                            if gameField[openTile].neighborBombs == 0:
                                checkList.append(openTile)

        #print("reached end of zero check")

        return tileList

    def checkZerosCorner(self, gameField, adjTiles, checkCondition):

        cornerList = []

        match checkCondition:
            case "tl":
                #print("topleft corner")
                cornerList.append(adjTiles[4])
                cornerList.append(adjTiles[6])
                cornerList.append(adjTiles[7])
            case "tr":
                #print("topright corner")
                cornerList.append(adjTiles[3])
                cornerList.append(adjTiles[5])
                cornerList.append(adjTiles[6])
            case "bl":
                #print("bottomleft corner")
                cornerList.append(adjTiles[1])
                cornerList.append(adjTiles[2])
                cornerList.append(adjTiles[4])
            case "br":
                #print("bottomright corner")
                cornerList.append(adjTiles[0])
                cornerList.append(adjTiles[1])
                cornerList.append(adjTiles[3])

        return cornerList

    def checkZerosWall(self, gameField, adjTiles, checkCondition):

        wallList = []

        match checkCondition:
            case "top":
                #print("top wall")
                wallList.append(adjTiles[3])
                wallList.append(adjTiles[4])
                wallList.append(adjTiles[5])
                wallList.append(adjTiles[6])
                wallList.append(adjTiles[7])
            case "btm":
                #print("bottom wall")
                wallList.append(adjTiles[0])
                wallList.append(adjTiles[1])
                wallList.append(adjTiles[2])
                wallList.append(adjTiles[3])
                wallList.append(adjTiles[4])
            case "lft":
                #print("left wall")
                wallList.append(adjTiles[1])
                wallList.append(adjTiles[2])
                wallList.append(adjTiles[4])
                wallList.append(adjTiles[6])
                wallList.append(adjTiles[7])
            case "rgt":
                #print("right wall")
                wallList.append(adjTiles[0])
                wallList.append(adjTiles[1])
                wallList.append(adjTiles[3])
                wallList.append(adjTiles[5])
                wallList.append(adjTiles[6])

        return wallList