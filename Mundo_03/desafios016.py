import random
import time

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=-')

for c in range(0, jogos):
    numeros = random.sample(range(1, 61), 6)
    print(f'Jogo {c + 1}: {numeros}')
    time.sleep(0.5)

print('-=-=-= < BOA SORTE! > -=-=-=-')