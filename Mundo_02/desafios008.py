import random

pc = random.randint(1, 3)
print('''Suas opções:
[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Escolha sua jogada: '))

if jogador == 1:
    if pc == 1:
        print('EMPATE! Você jogou PEDRA e o computador jogou PEDRA.')
    elif pc == 2:
        print('VOCÊ PERDEU! Você jogou PEDRA e o computador jogou PAPEL.')
    else:
        print('VOCÊ VENCEU! Você jogou PEDRA e o computador jogou TESOURA.')
elif jogador == 2:
    if pc == 1:
        print('VOCÊ VENCEU! Você jogou PAPEL e o computador jogou PEDRA.')
    elif pc == 2:
        print('EMPATE! Você jogou PAPEL e o computador jogou PAPEL.')
    else:
        print('VOCÊ PERDEU! Você jogou PAPEL e o computador jogou TESOURA.')
elif jogador == 3:
    if pc == 1:
        print('VOCÊ PERDEU! Você jogou TESOURA e o computador jogou PEDRA.')
    elif pc == 2:
        print('VOCÊ VENCEU! Você jogou TESOURA e o computador jogou PAPEL.')
    else:
        print('EMPATE! Você jogou TESOURA e o computador jogou TESOURA.')