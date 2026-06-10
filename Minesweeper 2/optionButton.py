import pygame


class OptionButton():

    def __init__(self, rectangle, value, clicked):

        self.rectangle = rectangle
        self.value = value
        self.buttonClicked = clicked

    def click(self):

        setattr(self, "buttonClicked", True)


    def unclick(self):
        
        setattr(self, "buttonClicked", False)

    def resizeRectangle(self, input1, input2, input3, input4):

        self.rectangle = pygame.Rect(input1, input2, input3, input4)