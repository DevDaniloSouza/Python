from rich import print, inspect
from classes import Aluno, Professor, Funcionario

a1 = Aluno('Danilo', 21, 'Eng. de Software', 'T03')
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor('Carlos', 31, 'Geografia', 'Mestrado')
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario('Samanta', 28, 'Secretária', 'Administração')
f1.bater_ponto()
inspect(f1, methods=True)
