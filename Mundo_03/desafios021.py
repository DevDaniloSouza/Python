lista = []
media = 0

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

    if resposta == 'N':
        break

for p in lista:
    media += p['idade']

media /= len(lista)

print('=-=' * 20)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade do grupo é de {media:.2f} anos.')
print('=-=' * 20)

print('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()

print('Pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] > media:
        print(f'Nome: {p["nome"]}; Sexo: {p["sexo"]}; Idade: {p["idade"]}')