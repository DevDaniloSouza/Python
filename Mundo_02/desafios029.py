import random
vitorias = 0

print('Vamor Jogar Par ou Ímpar?')
while True:
    num = int(input('Escolha um número: '))
    escolha = input('Par ou Ímpar? [P/I] ').strip().upper()
    computador = random.randint(0, 10)
    soma = num + computador

    print(f'Computador jogou: {computador}')
    resultado = 'P' if soma % 2 == 0 else 'I'

    if escolha == resultado:
        print('Você venceu!')
        vitorias += 1
    else:
        break

print(f'Você venceu {vitorias} vezes.')