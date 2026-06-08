import pygame
import sys

import minefield
import minelayer
import tile

pygame.init()

screenSize = 720

screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption("Minesweeper in Python")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 30, 30)
LIGHT = (200,200,200)
DARK = (100,100,100)
BG = (60,25,60)

font = pygame.font.SysFont("Courier", 25)
smallFont = pygame.font.SysFont("Courier", 15)

def startMenu():

    textInput = "35"
    active = False

    #Establishing the rectangles to be drawn on screen
    playButton = pygame.Rect(280, 220, 180, 50)
    quitButton = pygame.Rect(300, 380, 140, 50)

    tenButton = pygame.Rect(280, 290, 40, 50)
    fifteenButton = pygame.Rect(325, 290, 40, 50)
    twentyfiveButton = pygame.Rect(370, 290, 40, 50)

    customButton = pygame.Rect(415, 290, 40, 50)
    textInputBox = pygame.Rect(420, 315, 30, 20)

    titleText = font.render("Minesweeper", True, WHITE)
    subtitleText = font.render("Now in Python!", True, WHITE)

    playText = font.render("Board Size", True, WHITE)
    quitText = font.render("Quit", True, WHITE)

    tenText = font.render("10", True, WHITE)
    fifteenText = font.render("15", True, WHITE)
    twentyfiveText = font.render("25", True, WHITE)

    customText = smallFont.render("Custom", True, WHITE)
    texttextInput = smallFont.render(textInput, True, BLACK)

    playText = font.render("Board Size", True, WHITE)
    quitText = font.render("Quit", True, WHITE)

    tenText = font.render("10", True, WHITE)
    fifteenText = font.render("15", True, WHITE)
    twentyfiveText = font.render("25", True, WHITE)

    customText = smallFont.render("Custom", True, WHITE)

    while True:

        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        #Drawing rectangles for the buttons on screen
        pygame.draw.rect(screen, DARK, playButton)
        pygame.draw.rect(screen, LIGHT if quitButton.collidepoint(mouse) else DARK, quitButton)

        pygame.draw.rect(screen, LIGHT if tenButton.collidepoint(mouse) else DARK, tenButton)
        pygame.draw.rect(screen, LIGHT if fifteenButton.collidepoint(mouse) else DARK, fifteenButton)
        pygame.draw.rect(screen, LIGHT if twentyfiveButton.collidepoint(mouse) else DARK, twentyfiveButton)

        pygame.draw.rect(screen, LIGHT if customButton.collidepoint(mouse) and not textInputBox.collidepoint(mouse) else DARK, customButton)
        pygame.draw.rect(screen, WHITE, textInputBox)

        #Rendering the text onto the buttons
        texttextInput = smallFont.render(textInput, True, BLACK)

        screen.blit(titleText, (265, 100))
        screen.blit(subtitleText, (250, 150))

        screen.blit(playText, playText.get_rect(center=playButton.center))
        screen.blit(quitText, quitText.get_rect(center=quitButton.center))

        screen.blit(tenText, tenText.get_rect(center=tenButton.center))
        screen.blit(fifteenText, fifteenText.get_rect(center=fifteenButton.center))
        screen.blit(twentyfiveText, twentyfiveText.get_rect(center=twentyfiveButton.center))

        screen.blit(texttextInput, texttextInput.get_rect(center=textInputBox.center))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if tenButton.collidepoint(mouse):
                    game(10)

                elif fifteenButton.collidepoint(mouse):
                    game(15)

                elif twentyfiveButton.collidepoint(mouse):
                    game(25)

                elif textInputBox.collidepoint(mouse):
                    active = True

                elif customButton.collidepoint(mouse) and len(textInput) > 0:
                    game(int(textInput))

                elif quitButton.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

                else:
                    active = False

            if event.type == pygame.KEYDOWN and active:

                if event.key == pygame.K_BACKSPACE and len(textInput) > 0:
                    textInput = textInput[:-1]
                elif event.unicode.isdecimal() and len(textInput) < 2:
                    textInput += event.unicode
                elif event.key == pygame.K_RETURN and len(textInput) > 0:
                    game(int(textInput))

        pygame.display.update()

def gameOver():

    while True:

        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        restartButton = pygame.Rect(300, 300, 140, 50)
        quitButton = pygame.Rect(300, 380, 140, 50)

        pygame.draw.rect(screen, LIGHT if restartButton.collidepoint(mouse) else DARK, restartButton)
        pygame.draw.rect(screen, LIGHT if quitButton.collidepoint(mouse) else DARK, quitButton)

        restartText = font.render("Restart", True, WHITE)
        quitText = font.render("Quit", True, WHITE)

        screen.blit(restartText, restartText.get_rect(center=restartButton.center))
        screen.blit(quitText, quitText.get_rect(center=quitButton.center))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if restartButton.collidepoint(mouse):
                    startMenu()

                if quitButton.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def gameWin():

    while True:

        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        restartButton = pygame.Rect(300, 300, 140, 50)
        quitButton = pygame.Rect(300, 380, 140, 50)

        pygame.draw.rect(screen, LIGHT if restartButton.collidepoint(mouse) else DARK, restartButton)
        pygame.draw.rect(screen, LIGHT if quitButton.collidepoint(mouse) else DARK, quitButton)

        winText = font.render("You Win! Yippee!", True, WHITE)
        restartText = font.render("Restart", True, WHITE)
        quitText = font.render("Quit", True, WHITE)

        screen.blit(winText, (300, 150))
        screen.blit(restartText, restartText.get_rect(center=restartButton.center))
        screen.blit(quitText, quitText.get_rect(center=quitButton.center))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if restartButton.collidepoint(mouse):
                    startMenu()

                if quitButton.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game(size):

    fakeMinefield = minefield.Minefield(size)
    currentMinefield = fakeMinefield

    ml = minelayer.Minelayer(size)

    pad = 5
    gap = 2
    buttonSize = (screenSize - ((pad * 2) + (gap * (size - 1)))) / size
    
    tilesRemainingCount = 0

    i = 0

    for i in range(len(fakeMinefield.field)):

        btnPosHgt = 5 + (buttonSize * (i % size)) + (gap + (i % size))
        
        btnPosWid = 5 + (buttonSize * (i // size)) + (gap * (i // size))
        
        fakeMinefield.field[i].button = pygame.Rect(btnPosHgt, btnPosWid, buttonSize, buttonSize)

    while True:

        pygame.event.pump()

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        screen.fill(BG)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                leftClick = False
                rightClick = False

                if event.button == 1:
                    leftClick = True
                    print("left ", end="")
                elif event.button == 3:
                    rightClick = True
                    print("right ", end="")
                print("click detected", end = "")

                btn1 = 0
                for btn1 in range(len(currentMinefield.field)):

                    if currentMinefield.field[btn1].button.collidepoint(mouse):
                        print(" at button ", btn1)

                        if currentMinefield == fakeMinefield:
                            mf = ml.layMines(btn1)
                            currentMinefield = mf
                            for btnLocation in range(len(mf.field)):
                                mf.field[btnLocation].button = fakeMinefield.field[btnLocation].button

                            currentMinefield.field[btn1].clickTile()
                            adjacentZeroTiles = currentMinefield.checkForZeros(currentMinefield.field, btn1, size, [btn1])

                            #print(adjacentZeroTiles)

                            for tile in adjacentZeroTiles:
                                currentMinefield.field[tile].clickTile()

                        elif leftClick == False & rightClick == True & currentMinefield.field[btn1].clicked == False:
                            if currentMinefield.field[btn1].flagged == False:
                                print("Tile", btn1, "Flagged")
                            else:
                                print("Tile", btn1, "Unflagged")
                            currentMinefield.field[btn1].flagTile()

                        elif leftClick == True & rightClick == False & currentMinefield.field[btn1].flagged == True:
                            print("Tile", btn1, "currently flagged. Nothing changed.")     
                            
                        elif leftClick == True & rightClick == False & currentMinefield.field[btn1].clicked == True:
                            print("Tile already checked. Let's not tempt fate by checking again.")

                        elif leftClick == False & rightClick == True & currentMinefield.field[btn1].flagged:
                            print("I'm not going to flag an empty plot.")

                        elif (currentMinefield.field[btn1].flagged == False & currentMinefield.field[btn1].clicked == False & leftClick == True & rightClick == False):
                            print("Checking for bomb...")
                            
                            if currentMinefield.field[btn1].neighborBombs == 0 & currentMinefield.field[btn1].bomb == False:

                                if currentMinefield.field[btn1].clickTile():
                                    print("Bomb exploded! Game over!")
                                    gameOver()
                                else:
                                    currentMinefield.field[btn1].clickTile()
                                    adjacentZeroTiles = currentMinefield.checkForZeros(currentMinefield.field, btn1, size, [btn1])

                                    #print(adjacentZeroTiles)

                                    for tile in adjacentZeroTiles:
                                        currentMinefield.field[tile].clickTile()

                            else:

                                if currentMinefield.field[btn1].clickTile():
                                    print("Bomb exploded! Game over!")
                                    gameOver()
                                else:
                                    print("No bomb. Continue.")
                                    currentMinefield.field[btn1].clickTile()
                    
        btn = 0
        for btn in range(len(currentMinefield.field)):
            pygame.draw.rect(screen, LIGHT if currentMinefield.field[btn].clicked else DARK, currentMinefield.field[btn].button)

            if currentMinefield.field[btn].clicked:

                match currentMinefield.field[btn].neighborBombs:
                    case 0:
                        bombCounterColor = LIGHT
                    case 1:
                        bombCounterColor = (40, 150, 0)
                    case 2:
                        bombCounterColor = (0, 40, 150)
                    case 3:
                        bombCounterColor = (175, 155, 0)
                    case 4:
                        bombCounterColor = (200, 125, 20)
                    case 5:
                        bombCounterColor = RED
                    case 6:
                        bombCounterColor = RED
                    case 7:
                        bombCounterColor = RED
                    case 8:
                        bombCounterColor = RED
                
                shownNumber = font.render(str(currentMinefield.field[btn].neighborBombs), True, bombCounterColor)

                screen.blit(shownNumber, shownNumber.get_rect(center=currentMinefield.field[btn].button.center))

            if currentMinefield.field[btn].flagged:
                shownFlag = font.render("X", True, RED)
                screen.blit(shownFlag, shownFlag.get_rect(center=currentMinefield.field[btn].button.center))

        tilesRemainingCount = 0

        for btn2 in range(len(currentMinefield.field)):
            if currentMinefield.field[btn2].clicked == False:
                tilesRemainingCount += 1

        if tilesRemainingCount == len(ml.minesLaid):
            gameWin()

        pygame.display.update()

startMenu()
