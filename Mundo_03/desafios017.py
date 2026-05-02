alunos = []
aluno = []

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{(aluno[1] + aluno[2]) / 2:>8.1f}')