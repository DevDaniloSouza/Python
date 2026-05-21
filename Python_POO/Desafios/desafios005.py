from rich import print
from rich.panel import Panel

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.games = []

    def add_favoritos(self, game):
        self.games.append(game)

    def ficha(self):
        return Panel(f"Nome real: [blue]{self.nome}[/]\n"
                     f"Jogos Favoritos:",
                     title=f'Jogador <{self.nick}>', width=45)

j1 = Gamer('Danilo Pursino', 'PDS_PLAYER')
j1.add_favoritos('God of War II')
j1.add_favoritos('Far Cry 4')
j1.add_favoritos('Fallout 3')
j1.add_favoritos('GTA V')
print(j1.ficha())
