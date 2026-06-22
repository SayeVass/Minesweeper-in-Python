import datetime

class Timer():

    timeRemaining = datetime.time(0, 10, 0)

    lastCheckDatetime = datetime.datetime.now()

    def getTime(self):

        if (datetime.datetime.now() - self.lastCheckDatetime).total_seconds() >= 1 and self.timeRemaining > datetime.time(0,0,0):
            self.lastCheckDatetime = datetime.datetime.now()
            
            if self.timeRemaining.second == 0:
                self.timeRemaining = self.timeRemaining.replace(minute=self.timeRemaining.minute - 1, second=59)
            else:
                self.timeRemaining = self.timeRemaining.replace(second=self.timeRemaining.second - 1)

        return self.timeRemaining

    def getSecondsLeft(self):

        return self.timeRemaining