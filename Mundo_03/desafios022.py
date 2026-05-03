lista = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['gols'] = []
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
    
    lista.append(jogador)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

for jogador in lista:
    jogador['total'] = sum(jogador['gols'])

print('-=' * 30)
print(lista)
print('-=' * 30)

for jogador in lista:
    for k, v in jogador.items():
        print(f'{k.capitalize()}: {v}.')

print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if 0 <= busca < len(lista):
        jogador = lista[busca]
        print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
        for i, v in enumerate(jogador['gols']):
            print(f'    => Na partida {i + 1}, fez {v} gols.')
    else:
        print('Código do jogador inválido.')

    print('-=' * 30)

print('Programa encerrado. Volte sempre!')