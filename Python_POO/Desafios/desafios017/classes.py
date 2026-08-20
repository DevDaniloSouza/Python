from hashlib import sha256

class ContaBancaria:
    """Cria uma conta bancária e permite fazer saques e depósitos."""
    
    def __init__(self, id:int, nome:str = "Empty", saldo:float = 0, chave = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f'Conta {self._id} criada com sucesso. Saldo de R${self.__saldo:,.2f}.')

    def pede_senha(self):
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break

        return senha

    def validar_senha(self, chave):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo. Senha: {self.__hash}"
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado para conta {self._id}')

    def saque(self, valor:float, chave = None):

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque NEGADO de R${valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE')
            else:
                self.__saldo -= valor
                print(f'Saque de R${valor:.2f} autorizado para conta {self._id}')

        else:
            print("Senha inválida. Saque não autorizado!")


    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
        else:
            print("Senha não confere!")
