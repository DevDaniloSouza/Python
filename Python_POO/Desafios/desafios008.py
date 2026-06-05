from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.lado = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado)

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado * self.lado


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(raio)

    def perimetro(self):
        return 2 * 3.14159 * self.lado

    def area(self):
        return 3.14159 * self.lado ** 2


test = Circulo(20)

print(f'O perímetro do Polígono é de: {test.perimetro():.1f}.')
print(f'A área do Polígono é de: {test.area():.1f}')
