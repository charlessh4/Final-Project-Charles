import sys
from classes import *
file_out = open('terminal_output.txt','w')
sys.stdout = file_out
import csv
with open('mlb-player-stats-Batters.csv', 'r') as csvFile:
    readerNames = csv.reader(csvFile)
    batterNames = [line[0] for line in readerNames]
with open('mlb-player-stats-P.csv', 'r') as csvFile:
    readerNames = csv.reader(csvFile)
    pitcherNames = [line[0] for line in readerNames]
teams = ['Atlanta Braves', 'Miami Marlins', 'New York Mets', 'Philadelphia Phillies', 'Washington Nationals', 'Chicago Cubs', 
'Cincinnati Reds', 'Milwaukee Brewers', 'Pittsburgh Pirates', 'St. Louis Cardinals', 'Arizona Diamondbacks', 'Colorado Rockies', 'Los Angeles Dodgers',
'San Diego Padres', 'San Francisco Giants', 'Baltimore Orioles', 'Boston Red Sox', 'New York Yankees',
'Tampa Bay Rays', 'Toronto Blue Jays', 'Chicago White Sox', 'Cleveland Guardians', 'Detroit Tigers', 'Kansas City Royals', 'Minnesota Twins',
'Houston Astros', 'Los Angeles Angels', 'Oakland Athletics', 'Seattle Mariners', 'Texas Rangers']
divisions = ['NL East', 'NL Central', 'NL West', 'AL East', 'AL Central', 'AL West']
typeOfStat = 0
while typeOfStat != 5:
    print('Batter Stats: Enter 1\n Pitcher Stats: Enter 2\n Team Stats: Enter 3\n Division Stats: Enter 4\n Exit: Enter 5')
    typeOfStat = int(input())
    if(typeOfStat == 1): #Batting stats
        foundPlayer = -1
        print('Please enter the player you would like to analyze')
        player = input().lower()
        for i in batterNames:
            if i.lower() == player:
                foundPlayer = batterNames.index(i)
        if(foundPlayer == -1):
            print('Player not found please run again')
            break
        requestedPLayer = Batter(foundPlayer)
        print('Which stat of theirs would you like?\n 1: Hits, 2: At Bats, 3: Batting Average, 4: Strikeouts, 5: On Base Percentage, 6: Slugging ercentage')
        stat = int(input())
        if (stat == 1):
            print(requestedPLayer.getHits())
        elif (stat == 2):
            print(requestedPLayer.getAtBats())
        elif (stat == 3):
            print(requestedPLayer.getBattingAverage())
        elif (stat == 4):
            print(requestedPLayer.getStrikeOuts())
        elif (stat == 5):
            print(requestedPLayer.getOnBasePercentage())
        elif (stat == 6):
            print(requestedPLayer.getSluggingPercentage())
        else:
            print('Invalid input please try again and enter one of the options described above')
    elif(typeOfStat == 2): #Pitcher Stats
        foundPlayer = -1
        print('Please enter the player you would like to analyze')
        player = input().lower()
        for i in pitcherNames:
            if i.lower()== player:
                foundPlayer = pitcherNames.index(i)
        if(foundPlayer == -1):
            print('Player not found please run again')
            break
        requestedPLayer = Pitcher(foundPlayer)
        print('Which stat of theirs would you like?\n 1: Strikeouts, 2: ERA (Earned Run Average), 3: Wins')
        stat = int(input())
        if (stat == 1):
            print(requestedPLayer.getStrikeOuts())
        elif (stat == 2):
            print(requestedPLayer.getERA())
        elif (stat == 3):
            print(requestedPLayer.getWins())
        else:
            print('Invalid input please try again and enter one of the options described above')
    elif(typeOfStat == 3): #Team Stats
        foundTeam = -1
        print('Please enter the team you would like to analyze')
        requestedTeam = input().lower()
        for i in teams:
            if i.lower()== requestedTeam:
                foundTeam = teams.index(i)
        if(foundTeam == -1):
            print('Team not found please run again')
            break
        requestedTeam = Team(foundTeam)
        print('Which stat of theirs would you like?\n 1: Wins, 2: Losses, 3: World Series Wins')
        stat = int(input())
        if (stat == 1):
            print(requestedTeam.getWins())
        elif (stat == 2):
            print(requestedTeam.getLosses())
        elif (stat == 3):
            print(requestedTeam.getWSWins())
        else:
            print('Invalid input please try again and enter one of the options described above')
    elif(typeOfStat == 4): #Division Stats
        foundDivision = -1
        print('Please enter the division you would like to analyze')
        division= input().lower()
        for i in divisions:
            if i.lower()== division:
                foundDivision = divisions.index(i)
        if(foundDivision == -1):
            print('Division not found please run again')
            break
        requestedDivision = Division(foundDivision)
        print('Which stat of theirs would you like?\n 1: Wins, 2: Losses, 3: World Series Wins')
        stat = int(input())
        if (stat == 1):
            print(requestedDivision.getWins())
        elif (stat == 2):
            print(requestedDivision.getLosses())
        elif (stat == 3):
            print(requestedDivision.getWSWins())
        else:
            print('Invalid input please try again and enter one of the options described above')
    elif(typeOfStat > 5 or typeOfStat < 1): 
        print('Invalid input please enter one of the options described above')
    



