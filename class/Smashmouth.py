class NFLTeam:

    def __init__(self, team_name, list_players):
        self.team_name = team_name
        self.list_players = list_players

class Players:

    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition


player1 = Players("Joe Montana", "QB")
player2 = Players("Barry Sanders", "RB")
player3 = Players("Jerry Rice", "WR")
player4 = Players("Graham Gano", "K")

playerList = [player1, player2, player3, player4]

team1 = NFLTeam("Warriors", playerList)

print("\nTeam Name: {}".format(team1.team_name))
for player in team1.list_players:
    print(player.playerName)