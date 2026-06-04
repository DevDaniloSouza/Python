from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    sal_min = 1_621.00
    inss = 7.5

    def __init__(self):
        super().__init__()
        self.nome = ""
        self.sal_bruto = 0
        self.salario = 0

    def analizar_salario(self):
        painel = Panel(f'O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario / self.sal_min:.1f} salários mínimos.[/]', title="Análise de Salário", width=40)
        print(painel)

    @abstractmethod
    def calc_salario(self):
        pass


class Horista(Funcionario):
    def __init__(self,nome ,valor_hora, horas_trab):
        super().__init__()
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_salario(self):
        self.salario = self.horas_trab * self.valor_hora
        self.salario -= self.salario * self.inss / 100

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__()
        self.nome = nome
        self.sal_bruto = salario_bruto

    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)

