from rich import print
import time

class Livro:

    def __init__(self, titulo, paginas, pag=1):
        self.titulo = titulo
        self.paginas = paginas
        self.pag = pag
        print(self.__str__())

    def avancar_paginas(self, num):
        self.count(num)
        if self.fim():
            return f'[red]Você chegou ao final do Livro![/]'

    def count(self, paginas):
        for c in range(paginas):
            if not self.fim():
                self.pag += 1
                print(f'Pág{self.pag} > ', end='')
                time.sleep(0.3)
        print(f'[blue]Você agora está na [yellow]página {self.pag}[/]![/]')


    def fim(self):
        return True if self.pag == self.paginas else False
        
    def __str__(self):
        return f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.pag}[/].[/]"


liv = Livro('10 coisas que aprendi', 20)
print(liv.avancar_paginas(5))
print(liv.avancar_paginas(7))
print(liv.avancar_paginas(10))
