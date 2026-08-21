from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome) -> None:
        super().__init__()
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: 'QUACK! QUACK!'")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: 'AU! AU! AU!'")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: 'MIAU! MIAU!'")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: 'PÓ! PÓ! PÓ!'")

class PitBull(Cachorro):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: 'ROUF! ROUF!'")

class Spitz(Cachorro):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: 'au!au!au!au!au!au!'")
