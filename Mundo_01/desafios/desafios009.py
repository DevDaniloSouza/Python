import random

num = random.randint(0, 5)

print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')
palpite = int(input('Qual é o seu palpite? '))

if palpite == num:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! Você errou. O número era {}.'.format(num))