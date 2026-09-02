class Carteira:

    def __init__(self, valor:int|float = 0) -> None:
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.saldo:,.2f} na carteira."

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self):
        raise PermissionError("Você não tem autorização para alterar o saldo!")

    def __eq__(self, value) -> bool:
        if self.__saldo == value.__saldo:
            return True
        else:
            return False

    def __iadd__(self, value):
        self.__saldo = self.__saldo + value
        return self