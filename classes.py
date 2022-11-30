import csv
#This class initializes team data 
class Team:
    def __init__(self, i):
        index = i
        teamWins = [101, 69, 101, 87, 55, 74, 62, 86, 62, 93, 74, 68, 111, 89, 81, 83, 78, 99, 86, 92, 81, 92, 66, 65, 78, 106, 73,60, 90, 68]
        teamLosses = [61, 93, 61, 75, 107, 88, 100, 76, 100, 69, 88, 94, 51, 73, 81, 79, 84, 63, 76, 70, 81, 70, 96, 97, 84, 56, 89, 102, 72, 94]
        teamWorldSeries = [4, 2, 2, 2, 1, 3, 5, 0, 5, 11, 1, 0, 7, 0, 8, 3, 9, 27, 0, 2, 3, 2, 4, 2, 3, 2, 1, 9, 0, 0]
    def getWins(self):
        pass
    def getLosses(self):
        pass
    def getWSWins(self):
        pass
#This class is the child to teams as it uses the data from it to make its own list
class Division(Team):
    def __init__(self, i):
        index = i
        divisionWins = [sum(Team.teamWins[0:4]), sum(Team.teamWins[5:9]), sum(Team.teamWins[10:14]), sum(Team.teamWins[15:19]), sum(Team.teamWins[20:24]), sum(Team.teamWins[25:29])]
        divisionLosses = [sum(Team.teamLosses[0:4]), sum(Team.teamLosses[5:9]), sum(Team.teamLosses[10:14]), sum(Team.teamLosses[15:19]), sum(Team.teamLosses[20:24]), sum(Team.teamLosses[25:29])]
        divisionWorldSeries = [sum(Team.teamWorldSeries[0:4]), sum(Team.teamWorldSeries[5:9]), sum(Team.teamWorldSeries[10:14]), sum(Team.teamWorldSeries[15:19]), sum(Team.teamWorldSeries[20:24]), sum(Team.teamWorldSeries[25:29])]
    def getWins(self):
        return self.divisionWins[self.index]
    def getLosses(self):
        return self.divisionLosses[self.index]
    def getWSWins(self):
        return self.divisionWorldSeries[self.index]
#This class represents person and inherits the functions from coach while also having many unique functions
class Batter:
    def __init__(self, i): #i represents where the player is located in the list
        index = i-1 #Necessary due to titles for each column in csv
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            atBats = [line[5] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            hits = [line[7] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            sluggingPercentages = [line[21] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            onBasePercentages = [line[20] for line in readerNames]
        with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            strikeOuts = [line[15] for line in readerNames]
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
        index = i - 1 
        with open('mlb-player-stats-P.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            strikeOuts = [line[10] for line in readerNames]
        with open('mlb-player-stats-P.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            wins = [line[13] for line in readerNames]
        with open('mlb-player-stats-P.csv', 'r') as csvFile:
            readerNames = csv.reader(csvFile)
            earnedRunAverages = [line[18] for line in readerNames]
    def getStrikeOuts(self):
        return self.strikeOuts[self.index]
    def getERA(self): #Gets earned run average which is the average amount of runs a pitcher gives up per game in 2022
        return self.earnedRunAverages[self.index]
    def getWins(self):
        return self.wins[self.index]