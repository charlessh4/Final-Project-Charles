# Baseball Stats Getter

This program gathers statistics from mlb's stat database for all players that played in 2022 and all teams in the mlb. Player stats are only for this past year while teams and divisions have all time stats of wins losses and world series. Batters have the most stats consisting of hits, at bats, batting average, strikeouts, on base percentage, and slugging percentage. Then, pitchers have strikeouts, earned run average, and wins. All explanation for calculated stats are written in comments next to each method in the specific class. There are four classes filled with getter methods to get all the related stats of each object in the classes.py file. The team class parents the division class because that way the division can use the lists from the team class and add the stats of each team in each respective division into divisions' lists of stats. The main requests which stat the user would like and continuously runs in a while loop until the user wants to exit. The user will input an integer to get which object they would like to get stats of and then ask for which specific batter, pitcher, team, or division they would like and then ask for another int getting the specific stat. The program specifies to the user with print of what each integer will do so it is clear to all users. Lastly, if a player is not found the program will end, but if the input doesn't fit the will simply start the loop over again.

The Team class creates three lists containing all stats for the team and gets an index with each object creation to then know where in each list that requsted team's stat is. For each getter method it returns the respective stat using the created lists at the defined index of the object. The base idea of the index and lists with statisitcs is the same for all classes just using different stats. Then divisions inherits the teams class in order to created the division data by simply adding the team data together into each division of major league baseball. Both division and teams have the same getter methods of getWins, getLosses, and getWorldSeriesWins which do are only different due to being separate objects. The batter class has the same function of getter methods, but with hits, at bats, batting average, strikeouts, on base percentage, and slugging percentage this time. Additionally, for pitchers and batters their statistics are taken by reading in from separate csv files using csv methods and this is because there are over 700 players in the MLB making it much more efficient to download and import the data using csv. The pitcher class has getter methods for strikeouts, era, and wins and their data is put into lists as well utilizing csv, but from their own downloaded csv. 

In order to use this program once runnning the terminal will specify what each integer will do and then the user is required to input one that is specified, if it is not one specified it will ask to enter one that is described. Then, once the object they want stats of is selected the user must input the specific object they would like so specific player, team, or division exactly spelled correctly (case does not matter). Then the program will ask for which stat the user would like by intputting an int of the specific stat they would like. Below is a sample code of displaying the functions of the program.

Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
1
Please enter the player you would like to analyze
Xander Bogaerts
Which stat of theirs would you like?
 1: Hits, 2: At Bats, 3: Batting Average, 4: Strikeouts, 5: On Base Percentage, 6: Slugging ercentage
4
118
Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
2
Please enter the player you would like to analyze
Chris Sale
Which stat of theirs would you like?
 1: Strikeouts, 2: ERA (Earned Run Average), 3: Wins
1
5
Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
3
Please enter the team you would like to analyze
Boston Red Sox
Which stat of theirs would you like?
 1: Wins, 2: Losses, 3: World Series Wins
3
9
Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
4
Please enter the division you would like to analyze
NL Central
Which stat of theirs would you like?
 1: Wins, 2: Losses, 3: World Series Wins
1
284
Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
7
Invalid input please enter one of the options described above
Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
3
Please enter the team you would like to analyze
Chicago White Sox
Which stat of theirs would you like?
 1: Wins, 2: Losses, 3: World Series Wins
6
Invalid input please try again and enter one of the options described above
Batter Stats: Enter 1
 Pitcher Stats: Enter 2
 Team Stats: Enter 3
 Division Stats: Enter 4
 Exit: Enter 5
5

One feature that I would recommend in the future is past years stats of players and all time stats as then users could look at a much wider variety of stats. Another feature I would like to add is coach stats and more stats of player such as advanced statistics so that this can be a one stop program for any user that would like to know any stat of players, coaches, teams, and divisions quickly and easily.