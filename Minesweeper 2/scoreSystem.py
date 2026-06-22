import datetime
import math
import os

import scoreRecord

class ScoreSystem():

    def scoreCalculator(self, size, difficulty, timeLeft):

        match difficulty:
            case 10:
                diffMultiplier = 0.5
            case 5:
                diffMultiplier = 1
            case 4:
                diffMultiplier = 1.5

        secondsLeft = (timeLeft.second + (timeLeft.minute * 60))

        score = math.ceil(secondsLeft * (size / 100) * diffMultiplier)

        return score

    def scoreChecker(self, highScores, checkScore):

        for i in range(len(highScores)):
            if checkScore > int(highScores[i].getScore()):

                return True

        return False

    def scoreFormatter(self, highScores):

        scoreHolder = []
        for i in range(5):
            tempScore = scoreRecord.ScoreRecord(highScores[i*2], highScores[(i*2)+1])
            scoreHolder.append(tempScore)

        return scoreHolder

    def scoreLoader(self):

        if os.path.isfile("high.scores"):
            scorefile = open('high.scores')
            scores = scorefile.read()
            highScores = scores.split(",")
            scorefile.close()
            if len(highScores) != 10:
                defaultScores = open('high.scores', 'w')
                defaultScores.truncate(0)
                defaultScores.write("Empty,0,Empty,0,Empty,0,Empty,0,Empty,0")
                defaultScores.close()
                print("High score table corrupted. Empty high score table generated")
                
                scorefile = open('high.scores')
                scores = scorefile.read()
                highScores = scores.split(",")
                scorefile.close()

                highScores = self.scoreFormatter(highScores)
                return highScores
            else:
                highScores = self.scoreFormatter(highScores)
                return highScores
        else:
            defaultScores = open('high.scores', 'w')
            defaultScores.write("Empty,0,Empty,0,Empty,0,Empty,0,Empty,0")
            defaultScores.close()
            print("No high score table found. Empty high score table generated")
            
            scorefile = open('high.scores')
            scores = scorefile.read()
            highScores = scores.split(",")
            scorefile.close()

            highScores = self.scoreFormatter(highScores)
            return highScores
    
    def scoreUpdater(self, highScores, name, score):

        for record in range(5):

            if score > int(highScores[record].getScore()):
            
                for item in range(len(highScores)-1, record, -1):
                    if item > 0:

                        highScores[item] = highScores[item-1]
                
                break

        highScores[record] = scoreRecord.ScoreRecord(name, score)

        return highScores

    def scoreWriter(self, highScores):

        scoreFile = open('high.scores', 'w')
        scoreFile.truncate(0)
        scoreFile.close()

        scoreFile = open('high.scores', 'a')
    
        for i in range(len(highScores)):
            scoreFile.write(str(highScores[i].getName()))
            scoreFile.write(",")
            scoreFile.write(str(highScores[i].getScore()))

            if i < len(highScores) - 1:
                scoreFile.write(",")

        print("High score table updated.")
