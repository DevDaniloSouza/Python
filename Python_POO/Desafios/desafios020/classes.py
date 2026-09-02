from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, tamanho:int, ext = None, NomeComp = None) -> None:
        super().__init__()
        self.nome = nome
        self.tamanho = tamanho
        self._extensao = ext
        self.nome_completo = NomeComp

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, valor):
        self._extensao = valor

    @abstractmethod
    def abrir_arquivo(self):
        pass


class DOC(Arquivo):
    def __init__(self, nome: str, tamanho: int, ext=None, NomeComp=None) -> None:
        super().__init__(nome, tamanho, ext, NomeComp)

    def abrir_arquivo(self):
        format = self.tamanho / (1024 * 1024)
        self.extensao = format
        print(f'Abrindo o arquivo "{self.nome}.docx"({self.extensao:.2f}MB) no Microsoft Word.')


class PDF(Arquivo):
    def __init__(self, nome: str, tamanho: int, ext=None, NomeComp=None) -> None:
        super().__init__(nome, tamanho, ext, NomeComp)

    def abrir_arquivo(self):
        format = self.tamanho / (1024 * 1024)
        self.extensao = format
        print(f'Abrindo o arquivo "{self.nome}.pdf"({self.extensao:.2f}MB) no Adobe Reader.')

