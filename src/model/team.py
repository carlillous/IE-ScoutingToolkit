class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        player.set_team(self)

    def __str__(self):
        players_str = "\n".join(str(player) for player in self.players)
        return f"Equipo: {self.name}\nJugadores:\n{players_str}"