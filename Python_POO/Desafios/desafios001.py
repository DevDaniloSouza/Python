from rich import print

class Funcionario:
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}!'
    
f1 = Funcionario('Mateus', 'Administração', 'Diretor')
print(f1.apresentacao())

f2 = Funcionario('Ana Paula', 'Transporte', 'Gestora')
print(f2.apresentacao())
