import random

lista = []

def sorteio():
    for _ in range(5):
        lista.append(random.randint(1, 10))

def somaPar():
    return sum(x for x in lista if x % 2 == 0)

sorteio()
print(f'Os números sorteados foram: {lista}')
print(f'A soma dos números pares é: {somaPar()}')