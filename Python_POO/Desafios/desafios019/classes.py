from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str = "", salario:float = 1_621) -> None:
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if (valor > self._salario):
            self._salario = valor
        else:
            raise PermissionError("Você não pode diminuir o salário de um Funcionário!")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self) -> str:
        return f"Funcionário tipo: {self.__class__.__name__}. Nome: '{self.nome}'. Salário: {self.salario:.2f}"


class Gerente(Funcionario):
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)

    def calcular_bonus(self): # Aumento de 15%
        bonus = self.salario * 0.15
        self.salario = self.salario + bonus
        print(f"{self.nome} recebeu um aumento de R${bonus:.2f}!")


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)

    def calcular_bonus(self): # Aumento de 10%
        bonus = self.salario * 0.10
        self.salario = self.salario + bonus
        print(f"{self.nome} recebeu um aumento de R${bonus:.2f}!")


class Desingner(Funcionario):
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)

    def calcular_bonus(self): # Aumento de 8%
        bonus = self.salario * 0.08
        self.salario = self.salario + bonus
        print(f"{self.nome} recebeu um aumento de R${bonus:.2f}!")

