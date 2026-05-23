from rich import print
import time

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.total_paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/].[/]")

    def avancar_paginas(self, qtd = 1):
        cont = 1
        for pg in range(qtd):
            if not self.fim():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} > ', end='')
                time.sleep(0.3)
                cont += 1
        print(f'[blue]Você avançou [green]{cont} páginas[/]. Você agora está na [yellow]página {self.pagina_atual}[/]![/]')
        if self.fim():
            print(f'[red]Você chegou ao fim do Livro "{self.titulo}"![/]')

    def fim(self):
        return True if self.pagina_atual == self.total_paginas else False

liv = Livro('10 coisas que aprendi', 20)
print(liv.avancar_paginas(5))
print(liv.avancar_paginas(7))
print(liv.avancar_paginas(10))
