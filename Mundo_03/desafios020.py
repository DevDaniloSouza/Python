jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
jogador['gols'] = []
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))

jogador['total'] = sum(jogador['gols'])

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'{k.capitalize()}: {v}.')

print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols.')

print('-=' * 30)
