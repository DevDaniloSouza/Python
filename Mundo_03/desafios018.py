aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['média'] = float(input(f'Média do aluno: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'{k.capitalize()}: {v}')
print('-=' * 30)
