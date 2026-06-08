import pygame

class Tile():
    
    clicked = False
    flagged = False
    bomb = False
    neighborBombs = 0

    button = pygame.Rect(0, 0, 0, 0)

    def clickTile(self):

        if self.bomb == True:
            return True
        else:
            self.clicked = True
            return False

    def flagTile(self):

        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True
