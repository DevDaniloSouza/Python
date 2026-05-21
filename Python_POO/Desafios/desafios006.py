from rich import print
from rich.panel import Panel

class Caneta:

    def __init__(self, cor):
        self.cor = cor
        self.tampa = True

    def destampar(self):
        if self.tampa == True:
            self.tampa = False
        else:
            print('A caneta já está destampada!')

    def tampar(self):
        if self.tampa == False:
            self.tampa = True
        else:
            print('A caneta já está tampada!')

    def escrever(self, msg):
        if self.tampa == True:
            print('A caneta está tampada!')
        else:
            if self.cor == 'azul':
                print(f'[blue]{msg}[/]', end=' ')
            elif self.cor == 'verde':
                print(f'[green]{msg}[/]', end=' ')
            elif self.cor == 'vermelha':
                print(f'[red]{msg}[/]', end=' ')

    def quebrar_linha(self, num):
        for c in range(num):
            print()


c1 = Caneta('azul')
c2 = Caneta('verde')
c3 = Caneta('vermelha')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(2)

c2.escrever('Olá, pequeno Gafanhoto!')
c3.escrever('Vamos exercitar!')
