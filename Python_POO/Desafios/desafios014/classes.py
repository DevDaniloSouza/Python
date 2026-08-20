from rich import print

class Diario():
    def __init__(self, senha = "7404"):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, msg):
        if isinstance(msg, str):
            self.__segredos.append(msg.strip())

    def ler(self, senha):
        if senha == self.__senha:
            print("[green]Diário Liberado:[/]")
            for item in self.__segredos:
                print(f'- {item}')
        else:
            raise PermissionError('A senha informada está incorreta!')

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha!")
    
    @senha.setter
    def senha(self, nova_senha):
        pass
