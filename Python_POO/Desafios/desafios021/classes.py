from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:float=0, fvalor=None) -> None:
        super().__init__()
        self._valor = valor
        self.fvalor = fvalor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @abstractmethod
    def pagar(self, tipo:Pagamento, valor: float):
        pass


class Boleto(Pagamento):
    def __init__(self, valor: float = 0, fvalor=None) -> None:
        super().__init__(valor, fvalor)

    def pagar(self, tipo, valor):
        tipo.valor = valor
        tipo.fvalor = f"R$ {tipo.valor:,.2f}"
        print(f"Pagamento CONFIRMADO de {tipo.fvalor} via {tipo.__class__.__name__}")


class PIX(Pagamento):
    def __init__(self, valor: float = 0, fvalor=None) -> None:
        super().__init__(valor, fvalor)

    def pagar(self, tipo, valor):
        tipo.valor = valor
        tipo.fvalor = f"R$ {tipo.valor:,.2f}"
        print(f"Pagamento CONFIRMADO de {tipo.fvalor} via {tipo.__class__.__name__}")


class Credito(Pagamento):
    def __init__(self, valor: float = 0, fvalor=None) -> None:
        super().__init__(valor, fvalor)

    def pagar(self, tipo, valor):
        tipo.valor = valor
        tipo.fvalor = f"R$ {tipo.valor:,.2f}"
        print(f"Pagamento CONFIRMADO de {tipo.fvalor} via {tipo.__class__.__name__}")


def finalizar_compra(objeto:Pagamento, valor):
    try:
        objeto.pagar(objeto, valor)
    except Exception as e:
        print(f"Não foi possível efetuar o Pagamento! Erro: {e}")

