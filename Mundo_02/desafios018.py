somaIdade = 0
mediaIdade = 0
maiorIdade = 0
mulheres = 0
nomeVelho = ''

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somaIdade += idade

    if c == 1 and sexo == 'M':
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'F':
        mulheres += 1

mediaIdade = somaIdade / 4
print('A média de idade do grupo é: {}'.format(mediaIdade))
print('O homem mais velho é {} com {} anos.'.format(nomeVelho, maiorIdade))
print('Quantidade de mulheres no grupo: {}'.format(mulheres))