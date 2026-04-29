valores = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

for pos, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa de números digitados: {sorted(valores)}')
print(f'Lista de números pares: {sorted(pares)}')
print(f'Lista de números ímpares: {sorted(impares)}')