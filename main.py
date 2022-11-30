import sys
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
    typeOfStat = input()
    if(typeOfStat == 1):
        print('Please enter the player you would like to analyze')