import csv
#This class initializes team data 
class Team:
    def __init__(self, i):
        self.index = i
        self.teamWins = [101, 69, 101, 87, 55, 74, 62, 86, 62, 93, 74, 68, 111, 89, 81, 83, 78, 99, 86, 92, 81, 92, 66, 65, 78, 106, 73,60, 90, 68]
        self.teamLosses = [61, 93, 61, 75, 107, 88, 100, 76, 100, 69, 88, 94, 51, 73, 81, 79, 84, 63, 76, 70, 81, 70, 96, 97, 84, 56, 89, 102, 72, 94]
        self.teamWorldSeries = [4, 2, 2, 2, 1, 3, 5, 0, 5, 11, 1, 0, 7, 0, 8, 3, 9, 27, 0, 2, 3, 2, 4, 2, 3, 2, 1, 9, 0, 0]
    def getWins(self):
        return self.teamWins[self.index]
    def getLosses(self):
        return self.getLosses[self.index]
    def getWSWins(self):
        return self.teamWorldSeries[self.index]
#This class is the child to teams as it uses the data from it to make its own list
class Division(Team):
    def __init__(self, i):
        divisionTeam = Team(0)
        self.index = i
        self.divisionWins = [sum(divisionTeam.teamWins[0:4]), sum(divisionTeam.teamWins[5:9]), sum(divisionTeam.teamWins[10:14]), sum(divisionTeam.teamWins[15:19]), sum(divisionTeam.teamWins[20:24]), sum(divisionTeam.teamWins[25:29])]
        self.divisionLosses = [sum(divisionTeam.teamLosses[0:4]), sum(divisionTeam.teamLosses[5:9]), sum(divisionTeam.teamLosses[10:14]), sum(divisionTeam.teamLosses[15:19]), sum(divisionTeam.teamLosses[20:24]), sum(divisionTeam.teamLosses[25:29])]
        self.divisionWorldSeries = [sum(divisionTeam.teamWorldSeries[0:4]), sum(divisionTeam.teamWorldSeries[5:9]), sum(divisionTeam.teamWorldSeries[10:14]), sum(divisionTeam.teamWorldSeries[15:19]), sum(divisionTeam.teamWorldSeries[20:24]), sum(divisionTeam.teamWorldSeries[25:29])]
    def getWins(self):
        return self.divisionWins[self.index]
    def getLosses(self):
        return self.divisionLosses[self.index]
    def getWSWins(self):
        return self.divisionWorldSeries[self.index]
#This class represents person and inherits the functions from coach while also having many unique functions
class Batter:
    def __init__(self, i): #i represents where the player is located in the list
        self.index = i+1 #Necessary due to titles for each column in csv
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.atBats = [line[5] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.hits = [line[7] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.sluggingPercentages = [line[21] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.onBasePercentages = [line[20] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.strikeOuts = [line[15] for line in readerNames]
    def getHits(self):
        return self.hits[self.index]
    def getAtBats(self):
        return self.atBats[self.index]
    def getBattingAverage(self): # dividing a player's hits by his total at-bats for a number between zero (shown as . 000) and one (1.000)
        return self.hits[self.index]/self.atBats[self.index]
    def getStrikeOuts(self):
        return self.strikeOuts[self.index]
    def getOnBasePercentage(self): # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)
        return self.onBasePercentages[self.index]
    def getSluggingPercentage(self): #Equation: (1B + 2Bx2 + 3Bx3 + HRx4)/AB
        return self.sluggingPercentages[self.index]
class Pitcher:
    def __init__(self, i):
        self.index = i + 1 
        with open('mlb-player-stats-P.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.strikeOuts = [line[10] for line in readerNames]
        with open('mlb-player-stats-P.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.wins = [line[13] for line in readerNames]
        with open('mlb-player-stats-P.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            self.earnedRunAverages = [line[18] for line in readerNames]
    def getStrikeOuts(self):
        return self.strikeOuts[self.index]
    def getERA(self): #Gets earned run average which is the average amount of runs a pitcher gives up per game in 2022
        return self.earnedRunAverages[self.index]
    def getWins(self):
        return self.wins[self.index]