from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        pass
    
    def ferver_agua(self):
        pass

    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        pass

    def servir(self):
        pass


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        pass

    def servir(self):
        pass


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        pass

    def servir(self):
        pass