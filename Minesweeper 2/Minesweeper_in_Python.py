import os
import pygame
import sys

import minefield
import minelayer
import optionButton

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

def startMenu(savedBoardSize, savedCustomSize, savedDifficulty):

    textInput = savedCustomSize
    active = False

    #Establishing the rectangles to be drawn on screen

    boardSizeButton = optionButton.OptionButton(pygame.Rect(screenSize / 10, (screenSize * .4) - 10, 180, 30), 0, False)    

    tenButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 230, (screenSize * .4) - 10, 40, 30), 10, False)
    fifteenButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 280, (screenSize * .4) - 10, 40, 30), 15, False)
    twentyfiveButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 330, (screenSize * .4) - 10, 40, 30), 25, False)

    customButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 380, (screenSize * .4) - 10, 40, 30), textInput, False)
    textInputBox = pygame.Rect((screenSize / 10) + 385, (screenSize * .4) - 5, 30, 20)

    difficultyButton = optionButton.OptionButton(pygame.Rect(screenSize / 10 , (screenSize / 2) - 10, 180, 30), 0, False)

    easyButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 230, (screenSize / 2) - 10, 80, 30), 10, False)
    normalButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 320, (screenSize / 2) - 10, 100, 30), 5, False)
    hardButton = optionButton.OptionButton(pygame.Rect((screenSize / 10) + 430, (screenSize / 2) - 10, 80, 30), 4, False)

    playButton = optionButton.OptionButton(pygame.Rect((screenSize / 2) - 160, (screenSize * .6) - 25, 140, 50), 0, False)
    quitButton = optionButton.OptionButton(pygame.Rect((screenSize / 2) + 20, (screenSize * .6) - 25, 140, 50), 0, False)

    saveButton = optionButton.OptionButton(pygame.Rect(screenSize - 205, screenSize - 35, 200, 30), 0, False)

    #Clicking the saved settings
    match savedBoardSize:
        case '10':
            tenButton.click()
        case '15':
            fifteenButton.click()
        case '25':
            twentyfiveButton.click()
        case _:
            customButton.click()
    
    match savedDifficulty:
        case '0':
            easyButton.click()
        case '1':
            normalButton.click()
        case '2':
            hardButton.click()

    #Setting up the text to be drawn on screen
    titleText = font.render("Minesweeper", True, WHITE)
    subtitleText = font.render("Now in Python!", True, WHITE)

    boardSizeText = font.render("Board Size", True, WHITE)

    tenText = font.render("10", True, WHITE)
    fifteenText = font.render("15", True, WHITE)
    twentyfiveText = font.render("25", True, WHITE)

    texttextInput = smallFont.render(str(customButton.value), True, BLACK)

    difficultyText = font.render("Difficulty", True, WHITE)

    easyText = font.render("Easy", True, WHITE)
    normalText = font.render("Normal", True, WHITE)
    hardText = font.render("Hard", True, WHITE)

    playText = font.render("Play", True, WHITE)
    quitText = font.render("Quit", True, WHITE)

    saveText = font.render("Save Settings", True, WHITE)

    screen.fill(BG)

    tick = 0

    while True:

        mouse = pygame.mouse.get_pos()

        #Drawing rectangles for the buttons on screen
        
        pygame.draw.rect(screen, DARK, boardSizeButton.rectangle)

        pygame.draw.rect(screen, LIGHT if tenButton.buttonClicked or tenButton.rectangle.collidepoint(mouse) else DARK, tenButton.rectangle)
        pygame.draw.rect(screen, LIGHT if fifteenButton.buttonClicked or fifteenButton.rectangle.collidepoint(mouse) else DARK, fifteenButton.rectangle)
        pygame.draw.rect(screen, LIGHT if twentyfiveButton.buttonClicked or twentyfiveButton.rectangle.collidepoint(mouse) else DARK, twentyfiveButton.rectangle)

        pygame.draw.rect(screen, LIGHT if customButton.buttonClicked == True or customButton.rectangle.collidepoint(mouse) and not textInputBox.collidepoint(mouse) else DARK, customButton.rectangle)
        pygame.draw.rect(screen, WHITE, textInputBox)

        pygame.draw.rect(screen, DARK, difficultyButton.rectangle)

        pygame.draw.rect(screen, LIGHT if easyButton.rectangle.collidepoint(mouse) or easyButton.buttonClicked else DARK, easyButton.rectangle)
        pygame.draw.rect(screen, LIGHT if normalButton.rectangle.collidepoint(mouse) or normalButton.buttonClicked else DARK, normalButton.rectangle)
        pygame.draw.rect(screen, LIGHT if hardButton.rectangle.collidepoint(mouse) or hardButton.buttonClicked else DARK, hardButton.rectangle)

        pygame.draw.rect(screen, LIGHT if playButton.rectangle.collidepoint(mouse) else DARK, playButton.rectangle)
        pygame.draw.rect(screen, LIGHT if quitButton.rectangle.collidepoint(mouse) else DARK, quitButton.rectangle)

        pygame.draw.rect(screen, LIGHT if saveButton.rectangle.collidepoint(mouse) else DARK, saveButton.rectangle)

        #Rendering the text onto the buttons
        texttextInput = smallFont.render(str(customButton.value), True, BLACK)

        screen.blit(titleText, ((screenSize / 2) - (titleText.get_width() / 2) , (screenSize / 4) - (titleText.get_height() / 2)))
        screen.blit(subtitleText, ((screenSize / 2) - (subtitleText.get_width() / 2), (screenSize / 4) + (titleText.get_height() / 2) + 5))

        screen.blit(boardSizeText, boardSizeText.get_rect(center=boardSizeButton.rectangle.center))

        screen.blit(tenText, tenText.get_rect(center=tenButton.rectangle.center))
        screen.blit(fifteenText, fifteenText.get_rect(center=fifteenButton.rectangle.center))
        screen.blit(twentyfiveText, twentyfiveText.get_rect(center=twentyfiveButton.rectangle.center))

        if tick > 499 and active:
            texttextInput = smallFont.render(str(customButton.value) + "|", True, BLACK)
            screen.blit(texttextInput, texttextInput.get_rect(midleft=textInputBox.midleft))
        else:
            texttextInput = smallFont.render(str(customButton.value), True, BLACK)
            screen.blit(texttextInput, texttextInput.get_rect(midleft=textInputBox.midleft))

        tick = (tick + 1) % 999

        screen.blit(difficultyText, difficultyText.get_rect(center=difficultyButton.rectangle.center))

        screen.blit(easyText, easyText.get_rect(center=easyButton.rectangle.center))
        screen.blit(normalText, normalText.get_rect(center=normalButton.rectangle.center))
        screen.blit(hardText, hardText.get_rect(center=hardButton.rectangle.center))

        screen.blit(playText, playText.get_rect(center=playButton.rectangle.center))
        screen.blit(quitText, quitText.get_rect(center=quitButton.rectangle.center))

        screen.blit(saveText, saveText.get_rect(center=saveButton.rectangle.center))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if tenButton.rectangle.collidepoint(mouse):
                    tenButton.click()

                    active = False
                    fifteenButton.unclick()
                    twentyfiveButton.unclick()
                    customButton.unclick()

                elif fifteenButton.rectangle.collidepoint(mouse):
                    fifteenButton.click()

                    active = False
                    tenButton.unclick()
                    twentyfiveButton.unclick()
                    customButton.unclick()

                elif twentyfiveButton.rectangle.collidepoint(mouse):
                    twentyfiveButton.click()

                    active = False
                    tenButton.unclick()
                    fifteenButton.unclick()
                    customButton.unclick()

                elif textInputBox.collidepoint(mouse):
                    active = True
                    customButton.click()

                    tenButton.unclick()
                    fifteenButton.unclick()
                    twentyfiveButton.unclick()

                elif customButton.rectangle.collidepoint(mouse):
                    active = True
                    customButton.click()

                    tenButton.unclick()
                    fifteenButton.unclick()
                    twentyfiveButton.unclick()

                elif easyButton.rectangle.collidepoint(mouse):
                    easyButton.click()

                    normalButton.unclick()
                    hardButton.unclick()
                    active = False

                elif normalButton.rectangle.collidepoint(mouse):
                    normalButton.click()

                    easyButton.unclick()
                    hardButton.unclick()
                    active = False

                elif hardButton.rectangle.collidepoint(mouse):
                    hardButton.click()

                    easyButton.unclick()
                    normalButton.unclick()
                    active = False

                elif saveButton.rectangle.collidepoint(mouse):
                    boardSizeList = [tenButton, fifteenButton, twentyfiveButton, customButton]
                    difficultyList = [easyButton, normalButton, hardButton]

                    for sizeOption in boardSizeList:
                        if sizeOption.buttonClicked == True:
                            saveSize = sizeOption.value
                    
                    optionIndex = 0
                    for difficultyOption in difficultyList:
                        if difficultyOption.buttonClicked == True:
                            saveDifficulty = optionIndex
                        optionIndex += 1

                    savefile = open('settings.sav', 'w')
                    savefile.truncate(0)
                    savefile.close

                    savefile = open('settings.sav', 'a')
                    savefile.write(str(saveSize))
                    savefile.write(',')
                    savefile.write(str(customButton.value))
                    savefile.write(',')
                    savefile.write(str(saveDifficulty))
                    print("Current settings saved.")

                elif playButton.rectangle.collidepoint(mouse):
                    boardSizeList = [tenButton, fifteenButton, twentyfiveButton, customButton]
                    difficultyList = [easyButton, normalButton, hardButton]

                    for sizeOption in boardSizeList:
                        if sizeOption.buttonClicked == True:
                            gameBoardSize = sizeOption.value

                    for difficultyOption in difficultyList:
                        if difficultyOption.buttonClicked == True:
                            gameDifficulty = difficultyOption.value

                    game(int(gameBoardSize), gameDifficulty)

                elif quitButton.rectangle.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

                else:
                    active = False

            if event.type == pygame.KEYDOWN and active:

                if event.key == pygame.K_BACKSPACE and len(customButton.value) > 0:
                    customButton.value = customButton.value[:-1]
                elif event.unicode.isdecimal() and len(customButton.value) < 2:
                    customButton.value += event.unicode

        pygame.display.update()

def gameOverRender(mf, clickedTile, buttonSize):

    bomb = pygame.image.load('Bomb.png')
    bomb = pygame.transform.scale(bomb, (buttonSize, buttonSize))

    boom = pygame.image.load('Boom.png')
    boom = pygame.transform.scale(boom, (buttonSize, buttonSize))

    screen.fill(BG)

    for tile in range(len(mf.field)):
        pygame.draw.rect(screen, LIGHT if mf.field[tile].clicked else DARK, mf.field[tile].button)
    
        if mf.field[tile].clicked:

            match mf.field[tile].neighborBombs:
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
                
            shownNumber = font.render(str(mf.field[tile].neighborBombs), True, bombCounterColor)

            screen.blit(shownNumber, shownNumber.get_rect(center=mf.field[tile].button.center))

        elif mf.field[tile].bomb:

            if tile != clickedTile:
                screen.blit(bomb, bomb.get_rect(center=mf.field[tile].button.center))
            else:
                screen.blit(boom, boom.get_rect(center=mf.field[tile].button.center))
        
    gameOverBG = pygame.Surface([screenSize, screenSize], pygame.SRCALPHA, 32)
    gameOverBG = gameOverBG.convert_alpha()
    gameOverBG.fill((40, 40, 40, 100))

    screen.blit(gameOverBG, (0, 0))

def gameOver():

    while True:

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
                    gameLoader()

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
                    gameLoader()

                if quitButton.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game(size, difficulty):

    fakeMinefield = minefield.Minefield(size)
    currentMinefield = fakeMinefield

    ml = minelayer.Minelayer(size, difficulty)

    pad = 5
    gap = 2
    buttonSize = (screenSize - ((pad * 2) + (gap * (size - 1)))) / size
    
    redFlag = pygame.image.load('flag.png')
    redFlag = pygame.transform.scale(redFlag, (buttonSize, buttonSize))

    tilesRemainingCount = size * size

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
                            tilesRemainingCount -= 1
                            adjacentZeroTiles = currentMinefield.checkForZeros(currentMinefield.field, btn1, size, [btn1])

                            #print(adjacentZeroTiles)

                            for tile in adjacentZeroTiles:
                                currentMinefield.field[tile].clickTile()
                                tilesRemainingCount -= 1

                        elif leftClick == False & rightClick == True & currentMinefield.field[btn1].clicked == False:
                            if currentMinefield.field[btn1].flagged == False:
                                print("Tile", btn1, "Flagged")
                            else:
                                print("Tile", btn1, "Unflagged")
                            currentMinefield.field[btn1].flagTile()

                        elif leftClick == True & rightClick == False & currentMinefield.field[btn1].flagged:
                            print("Tile", btn1, "currently flagged. Nothing changed.")     
                            
                        elif leftClick == True & rightClick == False & currentMinefield.field[btn1].clicked:
                            print("Tile", btn, "already checked.")

                        elif leftClick == False & rightClick == True & currentMinefield.field[btn1].flagged:
                            print("I'm not going to flag an empty plot.")

                        elif (currentMinefield.field[btn1].flagged == False & currentMinefield.field[btn1].clicked == False & leftClick == True & rightClick == False):
                            print("Checking for bomb...")
                            
                            if currentMinefield.field[btn1].neighborBombs == 0 & currentMinefield.field[btn1].bomb == False:

                                if currentMinefield.field[btn1].clickTile():
                                    print("Bomb exploded! Game over!")
                                    gameOverRender(currentMinefield, btn1, buttonSize)
                                    gameOver()
                                else:
                                    currentMinefield.field[btn1].clickTile()
                                    tilesRemainingCount -= 1
                                    adjacentZeroTiles = currentMinefield.checkForZeros(currentMinefield.field, btn1, size, [btn1])

                                    #print(adjacentZeroTiles)

                                    for tile in adjacentZeroTiles:
                                        tilesRemainingCount -= 1
                                        currentMinefield.field[tile].clickTile()

                            else:

                                if currentMinefield.field[btn1].clickTile():
                                    print("Bomb exploded! Game over!")
                                    gameOverRender(currentMinefield, btn1, buttonSize)
                                    gameOver()
                                else:
                                    print("No bomb. Continue.")
                                    tilesRemainingCount -= 1
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

                screen.blit(redFlag, redFlag.get_rect(center=currentMinefield.field[btn].button.center))

        if tilesRemainingCount == len(ml.minesLaid):
            gameWin()

        pygame.display.update()

def gameLoader():

    if os.path.isfile("settings.sav"):
        savefile = open('settings.sav')
        save = savefile.read()
        savedSettings = save.split(",")
        savefile.close()
        if len(savedSettings) != 3:
            defaultSettings = open('settings.sav', 'w')
            defaultSettings.truncate(0)
            defaultSettings.write("15,35,1")
            defaultSettings.close()
            print("Saved settings corrupted. Overwritten with default settings.")
            gameLoader()
        else:
            startMenu(savedSettings[0], savedSettings[1], savedSettings[2])
    else:
        defaultSettings = open('settings.sav', 'w')
        defaultSettings.write("15,35,1")
        defaultSettings.close()
        print("No saved settings detected. Default saved settings generated.")
        gameLoader()

gameLoader()