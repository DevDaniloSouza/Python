from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        pass

    def receber_dano(self):
        pass

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = []

    def curar(self):
        pass


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = []

    def curar(self):
        pass

