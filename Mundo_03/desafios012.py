pessoas = list()
dados = list()
pesados =list()
leves = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        pesados = leves = dados[:]
    else:
        if dados[1] > pesados[1]:
            pesados = dados[:]
        if dados[1] < leves[1]:
            leves = dados[:]

    dados.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesados[1]}Kg. Peso de {pesados[0]}.')
print(f'O menor peso foi de {leves[1]}Kg. Peso de {leves[0]}.')