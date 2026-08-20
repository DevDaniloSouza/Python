from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int) -> None:
        super().__init__()
        self._nome = nome
        self._nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido!")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento!")

class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome, nasc, curso) -> None:
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O Curso {curso} não está na lista oficial de cursos!")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()

        if 3 <= len(curso) <=5 and curso not in Aluno.cursos_oficiais:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"O curso {curso} está fora do padrão para Cursos! Ou já existe na lista.")
