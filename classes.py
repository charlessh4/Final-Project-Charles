import pybaseball
#This class is the parent to teams as it carries the values of multiple teams 
class Division:
    def __init__(self):
        pass
    def getWins(self):
        pass
    def getLosses(self):
        pass
    def getWSWins(self):
        pass
#This carries all the same values from the division class thus is a child class
class Team(Division):
    def __init__(self):
        pass
#This class is a person so thus does not inherit from division or team 
class Coach:
    def __init__(self):
        pass
    def getWins(self):
        pass
    def getLosses(self):
        pass
    def getWSWins(self):
        pass
#This class represents person and inherits the functions from coach while also having many unique functions
class Player(Coach):
    def __init__(self):
        pass
    def getHits(self):
        pass
    def getAtBats(self):
        pass
    def getBattingAverage(self): # dividing a player's hits by his total at-bats for a number between zero (shown as . 000) and one (1.000)
        pass
    def getStrikeOuts(self):
        pass
    def getFieldingPercentage(self): #the total number of putouts and assists by a defender, divided by the total number of chances (putouts, assists and errors)
        pass
    def getOnBasePercentage(self): # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)
        pass
    def getSluggingPercentage(self): #Equation: (1B + 2Bx2 + 3Bx3 + HRx4)/AB
        pass
