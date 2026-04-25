import random

num = random.randint(0, 10)
print('Tente adivinhar o número que estou pensando entre 0 e 10.')
res = int(input('Digite o seu palpite: '))
tentativas = 1

while res != num:
    print('Número errado. Tente novamente.')
    res = int(input('Digite o seu palpite: '))
    tentativas += 1

if res == num:
    print('Parabéns! Você acertou o número {} em {} tentativas.'.format(num, tentativas))