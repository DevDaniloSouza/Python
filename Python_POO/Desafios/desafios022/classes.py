from rich.panel import Panel
from rich import print

class Mensagem:
    def __init__(self, msg, tipo="", icone="") -> None:
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(f"{self._mensagem}", title=f":bell: Aviso :bell:", width=40)
        print(msg)


class Erro(Mensagem):
    def __init__(self, msg, tipo="", icone="") -> None:
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        msg = Panel(f"{self._mensagem}", title=f":prohibited: Erro :prohibited:", width=40, style="red")
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg, tipo="", icone="") -> None:
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        msg = Panel(f"{self._mensagem}", title=f":warning: Alerta :warning:", width=40, style="yellow")
        print(msg)

