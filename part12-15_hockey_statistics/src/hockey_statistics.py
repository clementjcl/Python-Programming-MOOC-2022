import json

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f"{self.name:21}{self.team}{self.goals:>4} +{self.assists:>3} = {(self.goals)+(self.assists):>3}"
        
        
class HockeyStatistics():
    def __init__(self):
        self.__players = []
        
    def __points_scored(self, player: Player):
        return [(player.goals + player.assists), player.goals]
    
    def __goals_scored(self, player: Player):
        return [player.goals, (player.games)*-1]

    def read_file(self, file_name: str):
        with open(file_name) as stat_file:
            data = stat_file.read()    
        self.__players_data = json.loads(data)
        print(f"read the data of {len(self.__players_data)} players")
        for player in self.__players_data:
            self.__players.append(Player(player['name'], player['nationality'], player['assists'], player['goals'], player['penalties'], player['team'], player['games']))

        ###################################
        #for player in self.__players:
        #    print(player)
        ###################################

    def stat_by_name(self, name: str):
        for player in self.__players:
            if player.name == name:
                return player
        
    def teams(self):
        return sorted(set(list(map(lambda player: player.team, self.__players))))
    
    def countries(self):
        return sorted(set(list(map(lambda player: player.nationality, self.__players))))
            
    def players_in_team(self, team: str):
        return sorted(list(filter(lambda player: player.team == team, self.__players)), key=self.__points_scored, reverse=True)
            
    def players_from_country(self, country: str):
        return sorted(list(filter(lambda player: player.nationality == country, self.__players)), key=self.__points_scored, reverse=True)
    
    def most_points(self, num_players: int):
        players = sorted(self.__players, key=self.__points_scored, reverse=True)
        for i in range(0, num_players):
            print(players[i])

    def most_goals(self, num_players: int):
        players = sorted(self.__players, key=self.__goals_scored, reverse=True)
        for i in range(0, num_players):
            print(players[i])

class HockeyStatisticsApplication:
    def __init__(self):
        self.__statistics = HockeyStatistics()
        
    def read_file(self):
        file_name = input('file name: ')#'partial.json' #input('file name: ')
        self.__statistics.read_file(file_name)
        
    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    def search_for_player(self):
        name = input("name: ")
        print(self.__statistics.stat_by_name(name))
    
    def teams(self):
        for team in self.__statistics.teams():
            print(team)
    
    def countries(self):
        for country in self.__statistics.countries():
            print(country)        
        
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(player)
        
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(player)  
        
    def most_points(self):
        num_players = int(input("how many: "))
        self.__statistics.most_points(num_players)
    
    def most_goals(self):
        num_players = int(input("how many: "))
        self.__statistics.most_goals(num_players)

    def execute(self):
        self.read_file()
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.help()
                
# when testing, no code should be outside application except the following:
application = HockeyStatisticsApplication()
application.execute()