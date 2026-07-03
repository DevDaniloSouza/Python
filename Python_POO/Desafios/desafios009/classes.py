from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print(f'--- Iniciando o preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f'--- Bebida pronta ---')
    
    def ferver_agua(self):
        print(f'1. Fervendo água a 100° Celcius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print(f'2. Passando água pressurizada pelo pó de café muído.')

    def servir(self):
        print(f'3. Servindo em xícara pequena.')


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print(f'2. Mergulhando o sachê de ervas na água.')

    def servir(self):
        print(f'3. Servindo na caneca de porcelana com limão.')


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print(f'2. Passando vapor pressurizado pelo bico do leite')

    def servir(self):
        print(f'3. Servindo na caneca grande, já com café.')
