from abc import ABC, abstractmethod
from rich import print
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo:Personagem, forca):
        dano = random.randint(1, forca)
        golpe = random.randint(0, 2)
        print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com [blue]{self.golpes[golpe]}[/] de força {forca}.")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {dano}[/]!")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Pulo Giratório", "Chute"]

    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] tomou uma poção de cura e [green]recuperou {cura} pontos[/] de vida")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Mísseis Mágicos", "Bola de Fogo", "Cajado"]

    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida")

