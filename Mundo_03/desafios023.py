import random

jogo = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6),
}

ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)

for i, v in jogo.items():
    print(f'O {i} tirou {v} no dado.')

print('\nRanking dos jogadores:')
for i, (jogador, pontos) in enumerate(ranking, start=1):
    print(f'{i}º lugar: {jogador} com {pontos} pontos.')
