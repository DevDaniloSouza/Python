from rich import print
from rich.panel import Panel

class Churrasco:
    consumoCarne = 0.4
    precoCarne = 82.40

    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas

    def quantidade(self):
        return Churrasco.consumoCarne * self.pessoas
    
    def custo(self):
        return self.quantidade() * Churrasco.precoCarne
    
    def cada(self):
        return self.custo() / self.pessoas

    def analizar(self):
        return Panel(
            f'Analizando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados...[/]\n'
            f'Cada participante comerá {Churrasco.consumoCarne}Kg e cada Kg custa [red]R${Churrasco.precoCarne:.2f}[/].\n'
            f'Recomendo comprar [blue]{self.quantidade():.3f}Kg[/] de carne.\n'
            f'O custo total será de [green]R${self.custo():.2f}[/].\n'
            f'Cada pessoa pagará [blue]R${self.cada():.2f}[/] para participar.', 
            title=self.titulo, width=60)
    
c1 = Churrasco('Churras da Fotus', 30)
print(c1.analizar())

c2 = Churrasco('Churrasco Família', 10)
print(c2.analizar())

c3 = Churrasco('Churrasco da Ana', 2)
print(c3.analizar())
